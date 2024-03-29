from django.shortcuts import render
from rest_framework import generics
from .models import TutorflowModel, AnswersModel, TutorflowUsers, ForgotPassword, Favorites, likes, Feedbacks
from .serializers import TutorSerializer, AnswerSerializer, AnswerSerializer_RO, UserSerializer, FGPassSerializer
from .serializers import LoginSerializer, LikeSerializer, UserSerializerForPatch, FavoriteSerializer, FavoriteSerializerReadOnly, FeedbackSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from django_filters.rest_framework import DjangoFilterBackend

from django.conf import settings

from .services import send_email_verification, email_token

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
import jwt

import bcrypt
import secrets
import json

# Create your views here.
def get_hashed_password(plain_text_password):
    salt = bcrypt.gensalt(12)
    return bcrypt.hashpw(plain_text_password, salt)

def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)

def generate_6_digit_token():
    choices = '0123456789'
    token = ''
    for i in range(6):
        token += secrets.choice(choices)
    return token
# ----- User registarion API --------

# list all users
class ListAllUsersAPI(generics.ListAPIView):
    queryset = TutorflowUsers.objects.all()
    serializer_class = UserSerializer

class ListUsersAPI(APIView):
    '''
    data = {
            "firstname": user_first,
            "lastname": user_last,
            "email": user_email,
            "password": user_pass,
            "is_anon": True,
        }
    '''
    def post(self, request):
        ser = UserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        TutorflowUsers.objects.create_user(**ser.data)
        return Response('Created', status=status.HTTP_201_CREATED)

class GetUserAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = TutorflowUsers.objects.all()
    serializer_class = UserSerializerForPatch

# ----- User Login API --------
class AnonymousLoginAPI(APIView):
    def post(self, request):
        time = request.data['time']
        user_email, user_pass, user_first, user_last = 'user'+str(time)+'@email.com', "Temp@123", "User", time
        user_obj = TutorflowUsers()
        TutorflowUsers.objects.create_user(email=user_email, password=user_pass, firstname=user_first, lastname=user_last, is_anon=True)
        # user_obj.firstname = user_first
        # user_obj.lastname = user_last
        # user_obj.email = user_email
        # user_obj.password = user_pass
        # user_obj.is_anon = True
        # user_obj.save()
        data = {"email": user_email, "password": user_pass}
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            # serializer.save()
            # print("Serializer success mathod!", serializer.validated_data['user'])
            user = serializer.validated_data['user']
            token = RefreshToken.for_user(user)
            token.payload['superuser'] = user.is_superuser
            token.payload['anon_user'] = user.is_anon
            userObj = UserSerializer(user)
            user_data = {
                "id": userObj.data['id'],
                "firstname": userObj.data['firstname'],
                "lastname": userObj.data['lastname'],
                "email": userObj.data['email'],
                "is_anon": userObj.data['is_anon'],
                "is_active": userObj.data['is_active'],
                "is_superuser": userObj.data['is_superuser']
            }
            data = {
                'refresh': str(token),
                'access': str(token.access_token),
                'user': user_data
            }
            # print(data)
            return Response(data, status=status.HTTP_200_OK)
        return Response(False, status=status.HTTP_401_UNAUTHORIZED)

class LoginAPI(APIView):
    def post(self, request):
        # print("Post mathod!")
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # print("Serializer success mathod!", serializer.validated_data['user'])
            user = serializer.validated_data['user']
            token = RefreshToken.for_user(user)
            token.payload['superuser'] = user.is_superuser
            token.payload['anon_user'] = False
            userObj = UserSerializer(user)
            user_data = {
                "id": userObj.data['id'],
                "firstname": userObj.data['firstname'],
                "lastname": userObj.data['lastname'],
                "email": userObj.data['email'],
                "is_anon": userObj.data['is_anon'],
                "is_active": userObj.data['is_active'],
                "is_superuser": userObj.data['is_superuser']
            }
            data = {
                'refresh': str(token),
                'access': str(token.access_token),
                'user': user_data
            }
            # print(data)
            return Response(data, status=status.HTTP_200_OK)
        return Response(False, status=status.HTTP_401_UNAUTHORIZED)
    
class forgotPassword(APIView):
    '''
    1. verify posted email with existing users
    2. if verified, generate a token and save it in DB
    3. mail that token/code to the user
    4. when user enters the code, retrieve the code from the DB and verify it
    5. if yes, Let him reset the password
    6. else, raise error
    7. resetting - updating password in the user details
    '''
    def get(self, request):
        records = ForgotPassword.objects.all()
        serializer = FGPassSerializer(records, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        email = request.data['email']
        if_email_exists = TutorflowUsers.objects.filter(email = email)
        if if_email_exists:
            token = generate_6_digit_token()
            info = {
                "email": email,
                "token": token,
                "status": False
            }
            serializer = FGPassSerializer(data=info)
            if serializer.is_valid():
                serializer.save()
                email_token(email, token)
                return Response({"token_sent": True, "id": if_email_exists[0].id}, status=status.HTTP_201_CREATED)
        return Response({"token_sent":False})


class forgotPasswordPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForgotPassword.objects.all()
    serializer_class = FGPassSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class verifyToken(APIView):
    def post(self, request):
        email = request.data['email']
        token = request.data['token']
        try: record = ForgotPassword.objects.filter(email=email, status=False).first()
        except: return Response({"verified":False})
        if record.token == token:
            record.status = True
            record.save()
            return Response({"verified": True})
        return Response({"verified":False})

# ----- (Get, Post, Put, Delete, Update) Post(questions) API --------

class CreatePost(generics.ListCreateAPIView):
    queryset = TutorflowModel.objects.all()
    serializer_class = TutorSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['question', 'category', 'date_create', 'student']
    search_fields = ['question', 'category', 'student']
    ordering_fields = ['date_create']

class UpdatePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = TutorflowModel.objects.all()
    serializer_class = TutorSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# ----- (Get, Post, Put, Delete, patch) Answers and Answer readonly APIs --------

class ListAnswersAPI(generics.ListCreateAPIView):
    queryset = AnswersModel.objects.all()
    serializer_class = AnswerSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['question_id', 'answer', 'date_answered', 'topic', 'user', 'student_name']
    search_fields = ['question_id', 'answer', 'topic', 'user', 'student_name']
    ordering_fields = ['date_answered']

    def get_queryset(self):
        if self.request.query_params:
            qid = self.request.query_params.get('queid')
            # print("listAnswersAPI: ", qid)
            return AnswersModel.objects.filter(question_id=qid) # super().get_queryset()
        return AnswersModel.objects.all()

class GetAnswersAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswersModel.objects.all()
    serializer_class = AnswerSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        answer = AnswersModel.objects.get(id=pk)
        # print(request.data, answer, pk)
        isLiked = request.data['status']
        # print(isLiked)
        # Neutral
        if isLiked:
            answer.likes_count += 1
        else:
            answer.dislikes_count += 1
        answer.save()
        
        # print(answer.likes_count, answer.id)
        serializer = AnswerSerializer(AnswersModel.objects.get(pk=pk))
        return Response(serializer.data)

class ListAnswersAPI_RO(generics.ListCreateAPIView):
    queryset = AnswersModel.objects.all()
    serializer_class = AnswerSerializer_RO

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# ----------------
# (Get, Post, Put, Delete, patch) Favorites and favorites_readonly APIs; 
# Token Autherized; Restricted access to users
# -----------------

class ListFavoritesAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.headers.get('Authorization', None)
        try:
            if token: token = token.split(' ')[1]
            payload = jwt.decode(jwt = token, key = settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        user_id = payload.get('user_id', None)
        superuser = payload.get('superuser', False)
        if user_id and not superuser:
            user = TutorflowUsers.objects.get(id=user_id)
            favorites = Favorites.objects.filter(user=user)
            serializer = FavoriteSerializer(favorites, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if user_id and superuser:
            favorites = Favorites.objects.all()
            serializer = FavoriteSerializer(favorites, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        # print(request.data,'------_____---_-_---__-_----___--_---_--_-_-_--')
        user = data['user']
        question = data['question']
        serializer = FavoriteSerializer(data = {"user":user,"question":question})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetFavoritesAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListFavoritesAPI_RO(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.headers.get('Authorization', None)
        try:
            if token: token = token.split(' ')[1]
            payload = jwt.decode(jwt = token, key = settings.SECRET_KEY, algorithms=['HS256'])
            # print(payload)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        user_id = payload.get('user_id', None)
        superuser = payload.get('superuser', False)
        if user_id and not superuser:
            user = TutorflowUsers.objects.get(id=user_id)
            favorites = Favorites.objects.filter(user=user)
        if user_id and superuser: favorites = Favorites.objects.all()
        serializer = FavoriteSerializerReadOnly(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetFavoritesAPI_RO(generics.RetrieveDestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializerReadOnly

# ----------------
# (Get, Post, Put, Delete, patch) Likes API; 
# Token Autherized; Restricted access to users
# -----------------

class LikesAPI(generics.ListCreateAPIView):
    queryset = likes.objects.all()
    serializer_class = LikeSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # print(self.request.query_params)
        if self.request.query_params:
            status = self.request.query_params.get('status')
            uid = self.request.query_params.get('uid')
            if status is not None and not uid:
                likes_count = int(status)
                if likes_count == 1 or likes_count == 0:
                    return likes.objects.filter(status = likes_count)
                # print("List Likes records: ", id, likes_count)
            if status is not None and uid:
                likes_count = int(status)
                return likes.objects.filter(user=uid, status = likes_count)
            return likes.objects.filter(user=uid) # super().get_queryset()
        return likes.objects.all()
    
    def post(self, request):
        data = request.data
        # print(request.data,'------_____-?>>>>>>>>><>><><><>>>>>><<<<<<<--_--_-_-_--')
        user = data['user']
        answer = data['answer']
        s = data['status']
        serializer = LikeSerializer(data = {"user":user,"answer":answer, "status": s})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetLikesAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = likes.objects.all()
    serializer_class = LikeSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        # print("patch")
        data = likes.objects.get(pk = pk)
        answer = data.answer
        # print(answer)
        # print(answer.likes_count, answer.dislikes_count)
        if data.status == 0 and request.data['status'] == 1:
            # decrement dislikes count 
            # increment likes count 
            answer.likes_count += 1
            answer.dislikes_count -= 1
            answer.save()
        if data.status == 1 and request.data['status'] == 0:
            # increament dislikes count 
            # decrement likes count 
            answer.likes_count -= 1
            answer.dislikes_count += 1
            answer.save()
        # print(answer.likes_count, answer.dislikes_count)
        serializer = LikeSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# ----------------
# (Get, Post, Put, Delete, patch) Feedbacks API; 
# Basic Auth
# -----------------

@api_view(['GET', 'POST'])
def FeedbackAPI(request):
    if request.method == 'POST':
        serializer = FeedbackSerializer(data = request.data) # serializing the request data 
        if serializer.is_valid():
            serializer.save()
            send_email_verification(serializer['email'])
            return Response({"email":serializer['email'].value}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)
    else:
        data = Feedbacks.objects.all()
        serializer = FeedbackSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FeedbackDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbackSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

from rest_framework import serializers
from .models import TutorflowModel, AnswersModel, Users, ForgotPassword, Favorites, likes, Feedbacks
from .models import Users

from .services import send_email_verification


import bcrypt
import re

def get_hashed_password(plain_text_password):
    salt = bcrypt.gensalt(12)
    return bcrypt.hashpw(plain_text_password.encode(), salt)

def check_password(plain_text_password, hash):
    print("inside check")
    return bcrypt.checkpw(plain_text_password, hash)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'firstname', 'lastname', 'email', 'password','is_anon', 'is_active', 'is_superuser']
    
    def validate_password(self, value):
        hpass = get_hashed_password(value)
        return hpass
                
    def validate_email(self, value):
        email = value.strip().lower()
        if Users.objects.filter(email=email):
            raise serializers.ValidationError("Email address already exists!!!")
        return email

class UserSerializerForPatch(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
    
    def validate_password(self, value):
        hpass = get_hashed_password(value)
        return hpass

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(
        label="email",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, request):
        email = request.get('email')
        enteredpassword = request.get('password')
        if email and enteredpassword:
            user = Users.objects.filter(email = email).first()
            if user:
                password = user.password
                # print(check_password("ram", password), 4)
                if check_password(enteredpassword, password):
                    request['user'] = user
                    return request
                else:
                    msg = 'Password Mismatch'
                    raise serializers.ValidationError(msg, code='authorization')
            else:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
            # print(email, password, user, '++++++++++++++++++++++__________________')

        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')

class FGPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForgotPassword
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswersModel
        fields = ('id','answer','topic','student_name','links', 'question_id', 'date_answered', 'user','likes_count', 'dislikes_count') #'__all__'

class TutorSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = TutorflowModel
        fields = ('id', 'question', 'user', 'date_create', 'category', 'student', 'answers', 'mode') #'__all__'

class AnswerSerializer_RO(serializers.ModelSerializer):
    question_id = TutorSerializer(read_only=True)

    class Meta:
        model = AnswersModel
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = likes
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__'

class FavoriteSerializerReadOnly(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    question = TutorSerializer(read_only=True)
    class Meta:
        model = Favorites
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = '__all__'


# class TutorModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TutorModel
#         fields = '__all__'
    
#     def validate_email(self, email):
#         send_email_verification(email)
#         print("Email sent!!!!")
#         return email
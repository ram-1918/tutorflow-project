from rest_framework import serializers
from .models import TutorModel, TutorflowModel, AnswersModel, Users, Favorites, likes, Feedbacks
from .models import Users
from django.contrib.auth import authenticate

from .services import send_email_verification


import bcrypt
import re

# 12, in get=nsalt(), indicates slowness
# Slow is desirable because if a malicious party gets their hands on the table containing hashed passwords, 
# then it is much more difficult to brute force them.

def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt(12))

def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'firstname', 'lastname', 'email', 'is_anon', 'is_active', 'is_superuser']
    
    def validate_password(self, value):
        print("Plain: ", value)
        hpass = get_hashed_password(value)
        print("Hased: ", hpass)
        return hpass
                
    def validate_email(self, value):
        email = value.strip().lower()
        if Users.objects.filter(email=email):
            raise serializers.ValidationError("Email address already exists!!!")
        return email
    
class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * email
      * password.
    It will try to authenticate the user with when validated.
    """
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
        password = request.get('password')
        print(email, password, '++++++++++++++++++++++__________________')

        if email and password:
            user = Users.objects.filter(email = email).first()
            if not user:
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
            print(email, password, user, '++++++++++++++++++++++__________________')

        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        request['user'] = user
        return request

class AnswerSerializer(serializers.ModelSerializer):
    # question_id = TutorSerializer()

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

    # def create(self, validated_data):
    #     question_data = validated_data.pop('question_id')
    #     ans = AnswersModel.objects.create(**validated_data)
    #     ans.question_id = TutorflowModel.objects.create(**question_data)
    #     ans.save()
    #     return ans

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


class TutorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorModel
        fields = '__all__'
    
    def validate_email(self, email):
        send_email_verification(email)
        print("Email sent!!!!")
        return email
from datetime import datetime, timedelta
from django.conf import settings
import jwt
from .models import TutorflowModel, Users, Favorites, Feedbacks
from .serializers import TutorSerializer, UserSerializer, LoginSerializer, FavoriteSerializer, FavoriteSerializerReadOnly, FeedbackSerializer



def jwt_payload_handler(user):
    """
    Custom payload handler for JWT Authentication
    """
    return {
        'user_id': user.pk,
        'su': user.is_superuser,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(days=60),
        'orig_iat': datetime.utcnow(),
    }


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Custom response payload handler for JWT Authentication
    """
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }

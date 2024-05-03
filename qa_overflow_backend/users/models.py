from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email or not password:
            return ValueError('Email and Password are required to register.')
        # Creates new user with the given email id
        email = self.normalize_email(email)        # Normalize email with built-in method
        user = self.model(email=email, **kwargs)   # Calling its own model to create new user
        user.set_password(password)                # At this step, password should already be validated
        user.save()     # save the record to the DB
        return user
    

class Users(AbstractBaseUser):
    """
    id = uuid(custom)
    Firstname + lastname = 50 characters long
    Email: 50 chars long
    is_active = True, role = anon
    """
    roles = [('Admin', 'admin'), ('Regular', 'regular'), ('Anon', 'anon')]
    last_login = False
    
    objects = UserManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=25,blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=55, unique=True, blank=True)
    password = models.CharField(max_length=16, blank=True)
    role = models.CharField(max_length=10, choices=roles, default='regular')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        verbose_name_plural = 'Users'
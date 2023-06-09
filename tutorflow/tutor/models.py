from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)
    is_anon = models.BooleanField(default=False) # Is_anon - True initially, once loggedin - is_anon = False and replace the old token with the new one afterlogged in 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = 'Users'

class TutorflowModel(models.Model):
    options = [('python', 'Python'),
               ('java', 'Java'),
               ('sql', 'SQL'),
               ('web', 'WEB Technologies'),
               ('pyspark', 'PySpark'),
               ('django', 'Django'),
               ('vue', 'Vue'),
               ('aws', 'AWS'),
               ('ds', 'Data Science'),
               ('others', 'Others')]
    question = models.TextField(db_index=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    date_create = models.DateTimeField(auto_now = True)
    category = models.CharField(max_length = 255, choices=options, blank = True)
    student = models.CharField(max_length = 255, blank = True)
    mode = models.BooleanField(default=True)

    def __str__(self):
        return self.question if len(self.question) < 50  else self.question[:50]+'...'
    
    class Meta:
        verbose_name_plural = 'TutorflowModel'

class AnswersModel(models.Model):
    question_id = models.ForeignKey(TutorflowModel, on_delete=models.CASCADE, related_name="answers", null=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    answer = models.TextField(blank=True)
    date_answered = models.DateTimeField(auto_now = True)
    topic = models.CharField(max_length = 255, blank = True)
    student_name = models.CharField(max_length = 255, blank = True)
    links = models.CharField(max_length = 255, blank = True)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'AnswersModel'

class likes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswersModel, on_delete=models.CASCADE)
    status = models.IntegerField()

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name_plural = 'Favorites'

class Favorites(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.ForeignKey(TutorflowModel, on_delete=models.CASCADE)


    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name_plural = 'Favorites'

class Feedbacks(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    feedback = models.TextField()

    def __str__(self):
        return self.feedback
    
    class Meta:
        verbose_name_plural = 'Feedbacks'
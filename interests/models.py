from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username =  models.CharField(default='', max_length=50)
    email = models.EmailField(unique=True)
    region = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.email

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    data = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id}. {self.title}"

class Music(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id}. {self.title}"
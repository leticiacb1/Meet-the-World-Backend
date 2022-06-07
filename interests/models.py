from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserPersonalizado(AbstractUser):
    region=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.email}"


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    data = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    user = models.ForeignKey(UserPersonalizado, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.id}. {self.title}"

class Music(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    user = models.ForeignKey(UserPersonalizado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.title}"
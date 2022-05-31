from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100, primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=200)
    region = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.email}"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    data = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    userEmail = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.CharField(max_length=300, primary_key=True)
    def __str__(self):
        return f"{self.id}. {self.title} {self.userEmail}"

class Music(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    userEmail = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.CharField(max_length=300, primary_key=True)
    def __str__(self):
        return f"{self.id}. {self.title} {self.userEmail}"



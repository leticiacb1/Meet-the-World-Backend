from rest_framework import serializers
from .models import News, Music
from django.contrib.auth.models import User


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'content', 'data', 'link', 'user']

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['titulo', 'artista', 'img', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
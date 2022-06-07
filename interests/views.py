from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.http import Http404
from .models import Music,News
from rest_framework.decorators import api_view, permission_classes
from .serializers import MusicSerializer, NewsSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import UserPersonalizado as User


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_news(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist:
        raise Http404()

    if request.method == "DELETE":
        news.delete()
        return Response(status=204)

    serialized_news = NewsSerializer(news)
    return Response(serialized_news.data)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_music(request, music_id):
    try:
        music = Music.objects.get(id=music_id)
    except Music.DoesNotExist:
        raise Http404()
    
    if request.method == "DELETE":
        music.delete()
        return Response(status=204)

    serialized_music = MusicSerializer(music)
    return Response(serialized_music.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_news_get(request):

    if request.method == 'POST':
        new_news_data = request.data
        title = new_news_data['title']
        content = new_news_data['content']
        data = new_news_data['data']
        link = new_news_data['link']   
        user = request.user

        new_news = News(title=title, content=content, data=data, link=link, user=user)
        new_news.save()

    all_news = News.objects.filter(user=request.user)
    serialized_news = NewsSerializer(all_news, many=True)
    return Response(serialized_news.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_music_get(request):

    if request.method == 'POST':
        new_music_data = request.data
        titulo = new_music_data['titulo']
        artista = new_music_data['artista']
        img = new_music_data['img']
        user = request.user
        
        new_music = Music(titulo=titulo, artista=artista, img=img, user=user)
        new_music.save()

    all_music = Music.objects.filter(user=request.user)
    serialized_music = MusicSerializer(all_music, many=True)
    return Response(serialized_music.data)

@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            #print(f"Username: {username} Password: {password}")
            #user = User.objects.get(username=username)
            #print(user, user.username, user.password)
            user = authenticate(username=username, password='12345')
            print(user)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                print("ENtrou aqui")
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def api_get_users(request):

    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        #region = request.data['region']
        if User.objects.filter(email=email).exists() == False and User.objects.filter(username=username).exists() == False:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.is_staff=True
            user.save()
        else:
            return HttpResponseForbidden()
    all_users = User.objects.all()
    serialized_user = UserSerializer(all_users, many=True)
    return Response(serialized_user.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def api_get_user(request, username):
    if request.method == 'GET' and username != None:
        print(f"Username: {username}")
        user = User.objects.get(username=username)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data)
    else: 
        raise Http404()

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Music,News, CustomUser
from .serializers import MusicSerializer, NewsSerializer , CustomUserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from django.http import Http404, HttpResponseForbidden, JsonResponse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET', 'POST', 'DELETE'])
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
# @permission_classes([IsAuthenticated])
def api_news_get(request):

    if request.method == 'POST':
        new_news_data = request.data
        title = new_news_data['title']
        content = new_news_data['content']
        data = new_news_data['data']
        link = new_news_data['link']   

        new_news = News(title=title, content=content, data=data, link=link)
        new_news.save()

    all_news = News.objects.all()
    serialized_news = NewsSerializer(all_news, many=True)
    return Response(serialized_news.data)

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def api_music_get(request):

    if request.method == 'POST':
        new_music_data = request.data
        titulo = new_music_data['titulo']
        artista = new_music_data['artista']
        img = new_music_data['img']

        new_music = Music(titulo=titulo, artista=artista, img=img)
        new_music.save()

    try:
        all_music = Music.objects.all()
        serialized_music = MusicSerializer(all_music, many=True)
    except:
        raise  Response(status=204)

    return Response(serialized_music.data)


########## USER #############
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def api_users_get(request):
    if request.method == 'POST':
        new_User = CustomUser(**request.data)
        new_User.save()
    
        serialized_users = CustomUserSerializer(new_User)
        return Response(serialized_users.data)

@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            email = request.data['email']
            password = request.data['password']
            user = authenticate(email=email, password=password)
            print(email,password)
            print(user)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return Response(status=404)
                # return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()
    # try:
    #     if request.method == 'POST':
    #         email = request.POST.get('email')
    #         print(email)
    #         password = request.POST.get('password')
    #         print(password)
    #         user = authenticate(username=email, password=password)
        
    #         # if user is not None:
    #         #     token, created = Token.objects.get_or_create(user=user)
    #         #     return JsonResponse({"token":token.key})
    #         # else:
    #         return Response(status=200)
    # except:
    #     return Response(status=204)
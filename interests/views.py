from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Music,News
from .serializers import MusicSerializer, NewsSerializer

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
def api_music_get(request):

    if request.method == 'POST':
        new_music_data = request.data
        titulo = new_music_data['titulo']
        artista = new_music_data['artista']
        img = new_music_data['img']

        new_music = Music(titulo=titulo, artista=artista, img=img)
        new_music.save()

    all_music = Music.objects.all()
    serialized_music = MusicSerializer(all_music, many=True)
    return Response(serialized_music.data)
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/newss/<int:news_id>/', views.api_news),
    path('api/musics/<int:music_id>/', views.api_music),
    path('api/newss/', views.api_news_get),
    path('api/musics/', views.api_music_get),
]
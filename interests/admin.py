from django.contrib import admin
from .models import Music, News, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser,UserAdmin)
admin.site.register(Music)
admin.site.register(News)
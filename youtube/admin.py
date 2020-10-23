from django.contrib import admin
from .models import Video, Comment, Actor, Movie, Director
# Register your models here.

admin.site.register([Video, Comment, Actor, Movie, Director])

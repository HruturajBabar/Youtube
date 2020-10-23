from django.db import models
import datetime

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    path = models.CharField(max_length=60)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False) #todo: auto_now=True
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Actor(models.Model):
    actor_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class Movie(models.Model):
    movie_id = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    rating = models.FloatField(null=True, blank=True)
    genre =  models.CharField(max_length=30)

    def year_of_release():
        return [(r,r) for r in range(1984, datetime.date.today().year+1)]
    def current_year():
        return datetime.date.today().year
        choices = []
    year = models.IntegerField(('year'), choices=year_of_release(), default=current_year)

class Director(models.Model):
    direcctor_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)

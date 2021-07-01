from InternetMovieDatabase.settings import DEFAULT_AUTO_FIELD
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    upvoted = models.IntegerField()
    showcased = models.IntegerField()
    followers = models.IntegerField()
    created = models.IntegerField()
    collections = models.IntegerField()
    following = models.IntegerField()
    github = models.URLField(default="")

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    rating = models.IntegerField()
    photo = models.ImageField(
        upload_to='movie', default='defaultImg.png')

    def __str__(self):
        return self.name

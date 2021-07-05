from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField, URLField
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


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    rating = models.IntegerField()
    photo = models.ImageField(
        upload_to='movie', default='defaultImg.png')
    categories = models.ManyToManyField(Categories, blank=True)
    duration = IntegerField(default=0)
    trailer = URLField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + " - " + self.movie.name

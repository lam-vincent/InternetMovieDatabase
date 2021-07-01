from django.shortcuts import render
from .models import Person, Movie


def index(request):
    alex = Person.objects.first()
    contexte = {}
    contexte['person'] = alex
    contexte['github'] = alex.github
    return render(request, "movie/card.html", contexte)


def home(request):
    count = Movie.objects.count()
    movie_list = Movie.objects.all()
    contexte = {}
    contexte['movie_list'] = movie_list
    contexte['count'] = count
    print(Movie.objects.get(pk=2).photo)
    return render(request, "movie/home.html", contexte)


def movieDetails(request, id):
    details = Movie.objects.get(pk=id)
    contexte = {}
    contexte['details'] = details
    return render(request, "movie/movieDetails.html", contexte)

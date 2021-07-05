from django.db.models.fields.related import ForeignKey
from django.shortcuts import render
from .models import Comment, Person, Movie
from .forms import MovieForm
from django.shortcuts import redirect
from .utils import *


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
    contexte['categories'] = afficherCategories(details.categories.all())
    contexte['duration'] = conversionHeureMinute(details.duration)
    contexte['comments'] = Comment.objects.filter(movie=id)
    return render(request, "movie/movieDetails.html", contexte)


def addMovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = MovieForm()

    return render(request, 'movie/addMovie.html', {'form': form})


def removeMovie(request, id):
    m = Movie.objects.get(pk=id)
    m.delete()
    return redirect(home)

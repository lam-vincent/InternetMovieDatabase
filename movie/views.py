from django.shortcuts import render
from .models import Comment, Person, Movie
from .forms import MovieForm
from django.shortcuts import redirect
from .utils import *
from django.contrib.auth import authenticate, login as auth_login, logout


def index(request):
    alex = Person.objects.first()
    contexte = {}
    contexte['person'] = alex
    contexte['github'] = alex.github
    return render(request, "movie/card.html", contexte)


def home(request):
    count = Movie.objects.count()
    movie_list = Movie.objects.all()
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    contexte = {}
    contexte['movie_list'] = movie_list
    contexte['count'] = count
    contexte['username'] = username
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


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(home)
    return render(request, "movie/login.html")


def logout_view(request):
    logout(request)
    return redirect(loginView)

from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('profil', views.index, name="profil"),
    path('', views.home, name="index"),
    path('moviedetails/<int:id>/', views.movieDetails, name="movieDetails"),
    path('addmovie', views.addMovie, name="addMovie"),
    path('removemovie/<int:id>/', views.removeMovie, name="removeMovie"),
    path('login', views.loginView, name="login"),
    path('logout', views.logout_view, name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

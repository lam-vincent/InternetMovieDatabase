from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('profil', views.index, name="profil"),
    path('', views.home, name="index"),
    path('movieDetails/<int:id>/', views.movieDetails, name="movieDetails"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

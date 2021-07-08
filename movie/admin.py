from django.contrib import admin
from .models import Person, Movie, Categories, Comment, UserProfile

admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Categories)
admin.site.register(Comment)
admin.site.register(UserProfile)

# Là mảng chứa url của những cái app đó
from django.urls import path
from .views import current_datetime, random_people, random_game
urlpatterns = [
    path("test/", current_datetime, name = "current_datetime"),
    path("random_people/", random_people, name = "random_people"),
    path("random_game/", random_game, name = "random_game"),
]
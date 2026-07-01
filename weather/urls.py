from django.urls import path

from .views import (
    home,
    forecast,
    favorites,
    add_favorite,
    remove_favorite
)

urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "forecast/<str:city>/",
        forecast,
        name="forecast"
    ),

    path(
        "favorites/",
        favorites,
        name="favorites"
    ),

    path(
        "favorite/<str:city>/<str:country>/",
        add_favorite,
        name="add_favorite"
    ),

    path(
        "favorites/remove/<int:id>/",
        remove_favorite,
        name="remove_favorite"
    ),


]
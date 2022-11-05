from django.urls import path
from .views import Artistes, artistes_listing, Songs, songs_listing

urlpatterns = [
    path('artistes/', Artistes),
    path('artistes/<int:pk>', artistes_listing),
    path('songs/', Songs),
    path('songs/<int:pk>', songs_listing)
]
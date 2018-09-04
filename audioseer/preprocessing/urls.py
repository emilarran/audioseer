from django.urls import path
from preprocessing import views

urlpatterns = [
    # path('', views.ReadFromDataSetView.as_view(), name='read-from-data-set'),
    path('spotifyapi', views.SpotifyAPIView.as_view(), name='spotify-api'),
]

from rest_framework import serializers
from .models import MovieList

class Movieserialize(serializers.ModelSerializer):
    images = serializers.ImageField(max_length=None, use_url = True)
    class Meta:
        model = MovieList
        fields = ['id', 'name', 'movie_time', 'rating', 'images']
        
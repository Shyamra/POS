from django.shortcuts import render

from rest_framework import viewsets
from .serializers import Movieserialize
from .models import MovieList
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieList.objects.all()
    serializer_class = Movieserialize

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieList.objects.filter(typ = "action")
    serializer_class = Movieserialize

class ComboViewSet(viewsets.ModelViewSet):
    queryset = MovieList.objects.filter(typ = "combo")
    serializer_class = Movieserialize

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = MovieList.objects.filter(typ = "history")
    serializer_class = Movieserialize
    
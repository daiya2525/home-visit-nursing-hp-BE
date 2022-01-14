from django.shortcuts import render

from .models import News
from rest_framework import viewsets
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
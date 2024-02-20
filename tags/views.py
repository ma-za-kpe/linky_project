from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Tags
from .serializers import TagSerializer

class TagList(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer

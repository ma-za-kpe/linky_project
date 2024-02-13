from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Project, Link
from .serializers import ProjectSerializer


# use t viewsets and routers which address this issue and allow us to create the same API views and URLs with much less code
class ListProjects(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
class DetailProject(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
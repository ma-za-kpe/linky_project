from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Project, Link
from .serializers import ProjectSerializer, LinkSerializer
    
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
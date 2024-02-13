from django.urls import path
from .views import ListProjects, DetailProject
urlpatterns = [
    path('<int:pk>/', DetailProject.as_view()),
    path('', ListProjects.as_view()),
]
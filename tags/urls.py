from django.urls import path
from .views import TagList, TagDetail

urlpatterns = [
    path('tags/<int:pk>/', TagDetail.as_view()),
    path('tags', TagList.as_view()),
]

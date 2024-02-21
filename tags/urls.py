from django.urls import path
from .views import TagList, TagDetail

urlpatterns = [
    path('/', TagDetail.as_view()),
    path('', TagList.as_view()),
]
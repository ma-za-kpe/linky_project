from django.urls import path
from .views import TagList, TagDetail

urlpatterns = [

    path('', TagDetail.as_view()),  # While trying to create a new super_user I needed to remove the slash because it was throwing the following WARNINGS:
    # ?: (urls.W002) Your URL pattern '/' has a route beginning with a '/'. Remove this slash as it is unnecessary. 
    # If this pattern is targeted in an include(), ensure the include() pattern has a trailing '/'.
    path('', TagList.as_view()),
]

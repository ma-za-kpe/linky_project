from django.contrib import admin
from django.urls import path, include, re_path as re

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from rest_framework.schemas import get_schema_view 
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),  
    path('', include('profiles.urls')),  
    path('', include('tags.urls')),  
    path('api/auth/', include('authentication.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('docs.urls')),  
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
]

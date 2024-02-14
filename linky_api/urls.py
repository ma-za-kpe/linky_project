from django.contrib import admin
from django.urls import path, include

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
    path('api/', include('projects.urls')),  
    path('api/', include('profiles.urls')),  
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('docs.urls')),  
    #  move these two into docs app
    path(
        "linky-api/schema/",
        get_schema_view(
            title="Linky", 
            description="API for all things related to your project, providing a comprehensive interface for managing projects, links, and collaborators. Version 1.0.0 offers a robust set of endpoints for creating, updating, and accessing project details, along with functionalities for adding, managing, and categorizing links within projects. Explore the API to streamline your project management workflow and enhance collaboration", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    # path('api/docs/', include_docs_urls(title='Linky API')),
    # path('docs/', include_docs_urls(title='Blog API')), # new
]

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#  https://github.com/axnsan12/drf-yasg/?tab=readme-ov-file#installation
schema_view = get_schema_view(
   openapi.Info(
      title="Linky API",
      default_version='v1',
    description="API for all things related to your project, providing a comprehensive interface for managing projects, links, and collaborators. Version 1.0.0 offers a robust set of endpoints for creating, updating, and accessing project details, along with functionalities for adding, managing, and categorizing links within projects. Explore the API to streamline your project management workflow and enhance collaboration", version="1.0.0",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(
    #     r'^swagger(?P<format>\.json)$',
    #     schema_view.without_ui(cache_timeout=0),
    #     name='schema-json'
    # ),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

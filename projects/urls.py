from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProjectsViewSet, LinkViewSet
router = SimpleRouter()
router.register(r'projects', ProjectsViewSet)
router.register(r'links', LinkViewSet)
urlpatterns = router.urls
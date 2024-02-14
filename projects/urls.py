from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProjectsViewSet, LinkViewSet, TeamViewSet
router = SimpleRouter()
router.register(r'projects', ProjectsViewSet)
router.register(r'links', LinkViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = router.urls
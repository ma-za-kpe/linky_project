from rest_framework.routers import SimpleRouter
from .views import ProfileViewSet
router = SimpleRouter()
router.register(r'profiles', ProfileViewSet)
urlpatterns = router.urls

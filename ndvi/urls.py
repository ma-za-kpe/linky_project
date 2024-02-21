from rest_framework.routers import SimpleRouter
from .views import NdviViewSet
router = SimpleRouter()
router.register(r'ndvi', NdviViewSet)
urlpatterns = router.urls
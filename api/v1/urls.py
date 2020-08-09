from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ImageViewset, UserViewSet

router = DefaultRouter()
router.register('images', ImageViewset)
router.register('users', UserViewSet)

urlpatterns = router.urls

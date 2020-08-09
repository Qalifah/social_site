from rest_framework import viewsets
from images.models import Image
from django.contrib.auth import get_user_model
from .serializers import ImageSerializer, UserSerializer
from rest_framework.decorators import action

class ImageViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    #@action(methods=['get'], detail=True)
    #def personalise(self, request, *args, **kwargs):
    #    pass
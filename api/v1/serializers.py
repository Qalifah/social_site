from rest_framework import serializers
from images.models import Image
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class ImageSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    users_like = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'user', 'title','slug', 'url', 'image', 'description', 'created', 'users_like', 'total_likes')



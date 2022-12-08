from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):

    identity_no = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

from django.shortcuts import render
from users.serializers import UserSerializer
from users.models import User
from knox.models import AuthToken
from django.contrib.auth import authenticate

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes

@api_view(['POST'])
def resident_register(request):
    data = request.data

    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data

    user = User.objects.create(
        identity_no=data['identity_no'],
        name=data['name'],
        email=data['email'],
        password=data['password'],
    )

    token = AuthToken.objects.create(user)

    user = UserSerializer(user)

    print({"user":user, "token": token[1]})

    return Response(data={"user":user.data, "token": token[1]})


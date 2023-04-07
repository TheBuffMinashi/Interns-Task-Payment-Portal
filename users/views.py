from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User
from .utils import get_tokens_for_user
from .serializers import (
    UserSerializer, RegisterUserSerializer, LoginUserSerializer
)


class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()


class LoginUser(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(email=serializer.validated_data['email'])
            if user.check_password(serializer.validated_data['password']):
                message = {
                    'tokens': get_tokens_for_user(user),
                }
                return Response(message, status=status.HTTP_200_OK)
            else:
                message = {'login': 'your email or password is incorrect'}
                return Response(message, status=status.HTTP_401_UNAUTHORIZED)

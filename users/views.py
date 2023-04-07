from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import (
    UserSerializer, RegisterUserSerializer,
)


class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()

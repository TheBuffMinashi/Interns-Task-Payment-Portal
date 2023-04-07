from typing import Dict,Any

from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializer import UserLoginSerializer,UserRegisterSerializer

class RegisterUser(APIView):

    context:Dict[str,Any]

    def post(self,request) -> Response:
        
        user_register_serializer = UserRegisterSerializer(data = request.data)
        if user_register_serializer.is_valid():
            
            user = user_register_serializer.save()
            token:str = Token.objects.create(user = user).key

            self.context = {
                "message" : "User Registred Successfully ...",
                "token" : token,
            }

            return Response(self.context,status=status.HTTP_200_OK)



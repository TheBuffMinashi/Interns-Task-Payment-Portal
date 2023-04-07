from typing import Dict,Any

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

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
        
class LoginUser(APIView):

    context:Dict[str,Any]

    def post(self,request):
        
        user_login_serializer = UserLoginSerializer(data = request.data)
        if user_login_serializer.is_valid():

            entred_email:str = user_login_serializer.validated_data.get("email")
            
            user = User.objects.filter(email = entred_email).first()

            entred_password:str = user_login_serializer.validated_data.get("password")

            token:str = ""
            message:str = ""
            

            if user and check_password(entred_password,user.password):

                token = Token.objects.get_or_create(user = user)[0].key
                message = "Logging Successfully ..."
                status_code:int = status.HTTP_200_OK

            else:
                message = "Email or Password are not Correct !"
                status_code:int = status.HTTP_400_BAD_REQUEST

            self.context = {
                "message" : message,
                "token" : token
            }
            return Response(self.context,status=status_code)



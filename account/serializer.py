from typing import Dict,Any

from django.contrib.auth.models import User

from rest_framework import serializers

class UserAuthenticationSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length = 150,error_messages = {
        "required" : "Please Enter Email",
        "max_length" : "Entred Email is too long",
        "blank" : "Please Enter Email",
    })
    password = serializers.CharField(max_length = 100,min_length = 10,error_messages = {
        "required" : "Please Enter Password",
        "max_length" : "Entred Password is too long",
        "min_length" : "Entred Password is too short",
    })

class UserRegisterSerializer(UserAuthenticationSerializer):

    re_password = serializers.CharField(max_length = 100,min_length = 10,error_messages = {
        "required" : "Please Enter RePassword",
        "max_length" : "Entred RePassword is too long",
        "min_length" : "Entred Password is too short",
    })

    def validate(self,data:Dict[str,Any]):
        password:str = data.get("password","")
        re_password:str = data.get("re_password","")
        
        if password != re_password:
            raise serializers.ValidationError("Password and RePassword are not same !")
        return data

    def create(self,validated_data:Dict[str,Any]):
        email:str = validated_data.get("email")
        password:str = validated_data.get("password")

        self.__user = User(
            username = email,
            email = email,
        )
        self.__user.set_password(password)
        return self.__user

    @property
    def user(self):
        return self.__user


class UserLoginSerializer(UserAuthenticationSerializer):
    ...

from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView


class RegisterUser(APIView):

    def post(self,request):
        ...

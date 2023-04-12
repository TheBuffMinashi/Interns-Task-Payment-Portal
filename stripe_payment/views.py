from typing import Dict,Any

from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import CustomerSerializer,SetupIntentSerializer
from .payment.payment import Customer,PaymentIntent,SetupIntent




class NewCustomer(APIView):

    context:Dict[str,Any]

    permission_classes = (IsAuthenticated,)

    def post(self,request):

        customer_serializer = CustomerSerializer(request.data)

        if customer_serializer.is_valid():

            customer_serializer.save()

            name:str = customer_serializer.validated_data.get("name")
            describtion:str = customer_serializer.validated_data.get("describtion")
            email:str = customer_serializer.validated_data.get("email")
            phone:str = customer_serializer.validated_data.get("phone")

            Customer(
                name = name,
                describtion = describtion,
                email = email,
                phone = phone,
            ).create_new()

            self.context = {
                "message" : "Customer Added Successfully ..."
            }

            return Response(self.context,status=status.HTTP_200_OK)
        
        return Response(customer_serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    

    
class SetupIntent(APIView):

    permission_classes = (IsAuthenticated,)

    context:Dict[str,Any]

    def post(self,request):
        
        setup_intent_serializer = SetupIntentSerializer(request.data)

        if setup_intent_serializer.is_valid():
            setup_intent_serializer.save()

            self.context = {
                "message" : "SetupIntent Added Successfully ..."
            }

            return Response(
                self.context,
                status=status.HTTP_200_OK
            )
        return Response(data = setup_intent_serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)



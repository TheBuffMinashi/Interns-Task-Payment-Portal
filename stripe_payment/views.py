from typing import Dict,Any

from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializer import CustomerSerializer
from .payment.payment import Customer,PaymentIntent,SetupIntent


class NewCustomer(APIView):

    context:Dict[str,Any]

    permission_classes = (IsAuthenticated,)

    def post(self,request):

        customer_serializer = CustomerSerializer(request.data)

        if customer_serializer.is_valid():

            customer_serializer.save()

            Customer(
                name = customer_serializer.validated_data.get("name"),
                describtion = customer_serializer.validated_data.get("describtion"),
                email = customer_serializer.validated_data.get("email"),
                phone = customer_serializer.validated_data.get("phone"),
            ).create_new()

            self.context = {
                "message" : "Customer Added Successfully ..."
            }

            return Response(self.context,status=status.HTTP_200_OK)
        
        return Response(customer_serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    

    


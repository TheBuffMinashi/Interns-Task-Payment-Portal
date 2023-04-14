from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Payment
from .serializers import PaymentCreateSerializer


class PaymentCreateView(APIView):
    def post(self, request):
        serializer = PaymentCreateSerializer(
            data=request.data, context={'request': request})

        if serializer.is_valid():
            result = serializer.save()
            if result == True:
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePaymentStatusView(APIView):
    def get(self, request, token):
        payment = get_object_or_404(Payment.active, token=token)

        payment.paid = True

        payment.save()
        return Response({'msg': 'Your payment has been processed successfully.'})

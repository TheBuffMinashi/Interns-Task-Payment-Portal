from django.utils import timezone
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Payment
from .serializers import CreatePaymentSerializer


class CreatePaymentAPIView(CreateAPIView):
    serializer_class = CreatePaymentSerializer
    permission_classes = [AllowAny]


class ConfirmPaymentAPIView(APIView):
    def post(self, request):
        data = self.request.data
        payment_id = data.get('data').get('object').get('id')
        try:
            payment = Payment.objects.get(payment_id=payment_id)
        except Payment.DoesNotExist:
            raise ValidationError(detail='Invalid payment id')
        else:
            payment_type = data.get('type')
            if payment_type == 'payment_intent.succeeded':
                payment.status = payment.PaymentStatus.DONE
            elif payment_type == 'payment_intent.payment_failed':
                payment.status = payment.PaymentStatus.FAILED
            payment.date_modified = timezone.now()
            payment.save()
            response_data = {'detail': 'event received'}
            return Response(response_data, status=status.HTTP_200_OK)

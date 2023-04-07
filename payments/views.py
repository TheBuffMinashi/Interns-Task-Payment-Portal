from rest_framework.views import APIView
from rest_framework.response import Response
import stripe
from django.conf import settings
from payments.serializers import PaymentSerializer


class PaymentView(APIView):
    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        serializer = PaymentSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
        description = serializer.validated_data['description']
        token = request.data.get('token')
        email = request.data.get('email')
        payer_id = request.data.get('payer_id')

        charge = stripe.Charge.create(
            amount=int(amount * 100),  # convert to cents
            currency='usd',
            description=description,
            source=token,
            receipt_email=email
        )

        payment = serializer.save(stripe_charge_id=charge.id, paid=True, payer_id=payer_id)

        return Response(serializer.data)

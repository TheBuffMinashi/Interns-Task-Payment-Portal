import stripe

from rest_framework import serializers
from rest_framework.exceptions import APIException

from payment.models import Payment


class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount', 'currency', 'client_secret', 'status']
        read_only_fields = ['client_secret', 'status']

    def create(self, validated_data):
        payment = Payment(**validated_data)
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=payment.amount,
                currency=validated_data.get('currency'),
                # payment_method_types=['card'],
                automatic_payment_methods={
                    "enabled": True
                },
            )
        except stripe.error.StripeError as e:
            raise APIException
        else:
            payment.payment_id = payment_intent.id
            payment.client_secret = payment_intent.client_secret
            payment.status = Payment.PaymentStatus.REQUESTED
            payment.save()
        return payment

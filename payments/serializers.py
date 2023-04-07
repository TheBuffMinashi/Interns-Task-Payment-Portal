from rest_framework import serializers
from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'currency', 'description', 'created_at', 'stripe_charge_id', 'paid', 'payer_id']
        read_only_fields = ['created_at', 'stripe_charge_id', 'paid']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('Amount must be greater than 0')
        return value

    def validate_currency(self, value):
        if value.lower() not in ['usd', 'eur', 'gbp']:
            raise serializers.ValidationError('Invalid currency')
        return value.lower()

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError('Description is required')
        return value

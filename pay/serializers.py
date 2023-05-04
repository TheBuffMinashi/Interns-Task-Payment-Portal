from rest_framework import serializers
from pay.models import Payments

class PaymentSerializer(serializers.ModelSerializer):
    # user = serializers.Field(source='UserPay.username')
    user = serializers.ReadOnlyField(source='UserPay.username')

    class Meta:
        model = Payments
        fields = ('id', 'Transaction', 'Amount', 'Status', 'user', 'Time')
        

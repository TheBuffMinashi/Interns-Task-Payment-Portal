from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class SetupIntentSerializer(serializers.Serializer):

    desc = serializers.CharField(error_messages = {
        "required" : "Please Enter Describtion",
    })

    payment_method_types = serializers.ListField(error_messages = {
        "required" : "Please Enter Payment Method Types"
    })

from typing import Dict,Any

from rest_framework import serializers

from .models import Customer
from .models import SetupIntent as SetupIntentModel
from .payment.payment import SetupIntent

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

    customer_id = serializers.IntegerField(default = 0,error_messages = {
        "required" : "Please Enter Customer",
    })


    def create(self, validated_data:Dict[str,Any]):

        describtion:str = validated_data.get("desc")
        payment_method_types:str = validated_data.get("payment_method_types")
        customer_id:int = validated_data.get("customer_id",0)

        if not customer_id:
            raise serializers.ValidationError("Customer Is Not Valid ... !")
        
        customer = Customer.objects.filter(id = customer_id).first()

        if not customer:
            raise serializers.ValidationError("Customer Not Found ... !")
        
        setup_intent = SetupIntentModel(
            describtion = describtion,
            customer = customer
        )

        SetupIntent(
            payment_method_types = payment_method_types,
            customer = customer,
            describtion = describtion
        ).new_setup()


        return setup_intent

        

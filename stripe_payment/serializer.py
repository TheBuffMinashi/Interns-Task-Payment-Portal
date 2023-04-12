from typing import Dict,Any

from rest_framework import serializers

from .models import Customer,PaymentIntentModel
from .models import SetupIntent as SetupIntentModel
from .payment.payment import SetupIntent,PaymentIntent

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


class PaymentIntentSerializer(serializers.Serializer):

    describtion = serializers.CharField(
        error_messages = {
            "required" : "Please Enter Describtion"
        }
    )

    customer = serializers.IntegerField(
        default = 0,
    )

    currency = serializers.CharField(
        default = "pln"
    )

    amount = serializers.IntegerField(
        error_messages = {
            "required" : "Please Enter Amount ..."
        }
    )

    payment_method_types = serializers.ListField(
        error_messages = {
            "required" : "Please Enter Payment Method Types"
        }
    )

    capture_method = serializers.CharField(
        default = "manual"
    )


    def create(self, validated_data:Dict[str,Any]):
        
        customer_id:int = validated_data.get("customer",0)

        describtion:str = validated_data.get("describtion")

        amount:int = validated_data.get("amount")

        payment_method_types = validated_data.get("payment_method_types")

        currency = validated_data.get("currency")
        
        capture_method = validated_data.get("capture_method")

        if not customer_id:
            raise serializers.ValidationError("Customer Id is not Valid ... !")
        
        customer = Customer.objects.filter(id = customer_id).first()

        if not customer:
            raise serializers.ValidationError("Customer Not Found ... !")
        
        payment_intent_model = PaymentIntentModel(
            customer = customer,
            describtion = describtion,
            amount = amount,
            capture_method = capture_method,
            currency = currency
        )
        payment_intent_model.payment_method = payment_method_types


        PaymentIntent(
            describtion = describtion,
            customer = customer,
            amount = amount,
            currency = currency,
            payment_method_types = payment_method_types,
            capture_method = capture_method
        ).new_pay()


        

from rest_framework import serializers
from pay_module.models import Product, Order, LineItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        id = serializers.IntegerField()
        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
     class Meta:
        model = Order
        fields = "__all__"



class LineItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    order = OrderSerializers()

    class Meta:
        model = LineItem
        fields = [ 'order','product','price', 'quantity', 'date_added']

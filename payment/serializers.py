from rest_framework import serializers
from django.conf import settings
from products.models import Product

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionSerializer(serializers.Serializer):

    def create_checkout_stripe(self, product):
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': product.price,
                            'product_data': {
                                'name': product.name,
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
            )
            return checkout_session
        except Exception as e:
            return str(e)

    def save(self, **kwargs):
        product = Product.objects.filter(pk=self.context['pk']).first()
        if product:
            return self.create_checkout_stripe(product)
        return False

from rest_framework import serializers
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .models import Payment
from products.models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
import stripe

User = get_user_model()

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentCreateSerializer(serializers.Serializer):
    """
        TODO: Refactor this code to make the URL site dynamic instead of hardcoding it.
        Consider passing the URL as an argument to the function or retrieving it from
        a configuration file or environment variable.
    """
    product = serializers.IntegerField()
    quantity = serializers.IntegerField()
    url = serializers.URLField(default='http://127.0.0.1:8000')

    def checkout(self, product, token):
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': product.currency,
                    'product_data': {
                        'name': product.title,
                    },
                    'unit_amount': product.price * 100
                },
                'quantity': 1
            }],
            mode='payment',
            success_url=f'http://127.0.0.1:8000/api/payments/success/{token}',
            cancel_url='http://127.0.0.1:8000',
        )
        return checkout_session.url

    def save(self, **kwargs):
        product = get_object_or_404(
            Product.active, pk=self.validated_data['product'])

        # Creating a payment entry in the database to allow access to the token at a later time.
        payment = Payment.objects.create(
            product=product,
            user=User.objects.first(),
            currency=product.currency,
            total_price=product.price*self.validated_data['quantity'],
            quantity=self.validated_data['quantity'],
            is_active=True
        )

        # changing the default url with stripe checkout session url
        self.validated_data['url'] = self.checkout(
            product, token=payment.token)
        return True

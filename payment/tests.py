from django.urls import reverse
from rest_framework.test import APITestCase

from payment.models import Payment


class CreatePaymentTestCase(APITestCase):
    CREATE_ENDPOINT = 'create_payment'
    CONFIRM_PAYMENT_ENDPOINT = 'confirm_payment'

    def test_create_payment(self):
        # Testing signup user API
        self.data = {
            'amount': 5000,
            'currency': 'usd',
        }
        response = self.client.post(reverse(self.CREATE_ENDPOINT), self.data)
        self.assertEqual(response.status_code, 201)

        payment = Payment.objects.get(client_secret=response.data.get('client_secret'))
        self.assertEqual(payment.status, 'Requested')

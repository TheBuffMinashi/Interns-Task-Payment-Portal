import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from payments.models import Payment


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_payment(api_client):
    url = reverse('payment')
    data = {
        'amount': 10.00,
        'currency': 'usd',
        'description': 'Test payment',
        'token': 'tok_visa',
        'email': 'test@example.com',
        'payer_id': 'test_payer_id'
    }

    response = api_client.post(url, data=data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert Payment.objects.count() == 1

    payment = Payment.objects.first()
    assert payment.amount == 10.00
    assert payment.currency == 'usd'
    assert payment.description == 'Test payment'
    assert payment.paid is True
    assert payment.stripe_charge_id is not None
    assert payment.payer_id == 'test_payer_id'

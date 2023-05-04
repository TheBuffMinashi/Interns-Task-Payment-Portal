from django.test import TestCase
from .models import Payments,User
from django.urls import reverse
# Create your tests here.

class PaymentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='user1')
        Payments.objects.create(Amount=1000,Transaction="test",UserPay=user)
    def test_pay(self):
        payment = Payments.objects.get(Transaction="test")
        self.assertEqual(payment.Amount, 1000)
    def test_tempate(self):
        respo = self.client.get(reverse('index'))
        self.assertTemplateUsed(respo,'pay/index.html')

class PageUrlApi(TestCase):
    def setUp(self):
        user = User.objects.create(username='user2')
        Payments.objects.create(Amount=1200,Transaction="test2",UserPay=user)
    def test_url_api(self):
        respo = self.client.get(reverse('get_all'))
        self.assertEqual(respo.status_code, 200)
from typing import Dict,Any

from django.test import TestCase,Client

from . import views
from .models import Customer


class StripeSystemTestCase(TestCase):

    _SUCCESS_CODE:int = 200

    def setUp(self) -> None:
        
        self._client = Client(enforce_csrf_checks=True)
        
        self.__test_username:str = "admin"
        self.__test_password:str = "admin"

        self.__token_key:str = "f3247bc65d56855050ce63e9a1cfd36c68159402"

        state:bool = self._client.login(
            username = self.__test_username,
            password = self.__test_password
        )

        self._header:Dict[str,Any] = {
            "Authorization" : f"Token {self.__token_key}"
        }

    def _create_test_customer(self) -> Customer:
        customer_data:Dict[str,Any] = {
            "email" : "test@gmail.com",
            "describtion" : "test desc",
            "name" : "example name",
            "phone" : "09123456789",
        }

        customer = Customer.objects.create(
            **customer_data
        )

        return customer
        


class NewCustomerTestCase(StripeSystemTestCase):


    def test_new_customer(self):

        url:str = "/new-customer"


        data:Dict[str,Any] = {
            "email" : "test@gmail.com",
            "describtion" : "test desc",
            "name" : "example name",
            "phone" : "09123456789",
        }

        result = self._client.post(url,data,**self._header)


        self.assertEqual(result.status_code,self.__SUCCESS_CODE)


class SetupIntentTestCase(StripeSystemTestCase):

    def test_new_setup_intent(self):

        url:str = "/setup-intent"

        customer = self._create_test_customer()

        data:Dict[str,Any] = {
            "desc" : "Test Describtion",
            "payment_method_types" : ["a","b"],
            "customer_id" : customer.id,
        }

        response = self._client.post(
            url,data = data,**self._header
        )

        self.assertEqual(response.status_code,self._SUCCESS_CODE)


class PaymentIntentSerializer(StripeSystemTestCase):

    def test_new_payment(self):

        url:str = "/payment"

        customer = self._create_test_customer()

        data:Dict[str,Any] = {
            "describtion" : "Test Desc",
            "customer" : customer.id,
            "currency" : "pln",
            "amount" : 1000,
            "payment_method_types" : ["a","b"],
            "capture_method" : "manual"
        }

        response = self._client.post(
            url,data = data,**self._header
        )

        self.assertEqual(response.status_code,self._SUCCESS_CODE)

        
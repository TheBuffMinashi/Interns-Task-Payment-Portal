from typing import Dict,Any

from django.test import TestCase,Client

from . import views

class NewCustomerTestCase(TestCase):

    __SUCCESS_CODE:int = 200

    def setUp(self) -> None:
        
        self.__client = Client(enforce_csrf_checks=True)
        
        self.__test_username:str = "admin"
        self.__test_password:str = "admin"

        self.__token_key:str = "f3247bc65d56855050ce63e9a1cfd36c68159402"

        state:bool = self.__client.login(
            username = self.__test_username,
            password = self.__test_password
        )

        print(state)

        self.__header:Dict[str,Any] = {
            "Authorization" : f"Token {self.__token_key}"
        }

        self.__url:str = "/new-customer"

    def test_new_customer(self):

        data:Dict[str,Any] = {
            "email" : "test@gmail.com",
            "describtion" : "test desc",
            "name" : "example name",
            "phone" : "09123456789",
        }

        result = self.__client.post(self.__url,data,**self.__header)

        print(result.content)

        self.assertEqual(result.status_code,self.__SUCCESS_CODE)


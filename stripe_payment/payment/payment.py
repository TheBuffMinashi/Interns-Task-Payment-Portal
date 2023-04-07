import stripe

from .constant import STRIPE_KEY

class StripeManager:

    @classmethod
    def set_api_key(self) -> None:
        stripe.api_key = STRIPE_KEY

class Customer:

    def __init__(self,**information) -> None:
        
        self.__email:str = information["email"]
        self.__describtion:str = information["describtion"]
        self.__name:str = information["name"]
        self.__phone:str = information["phone"]

    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def describtion(self) -> str:
        return self.__describtion

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def phone(self) -> str:
        return self.__phone

    def create_new(self) -> stripe.Customer:

        stripe.Customer.create(
            email = self.__email,
            describtion = self.__describtion,
            name = self.__name,
            phone = self.__phone
        )
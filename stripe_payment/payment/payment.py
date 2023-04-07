from typing import Any,Dict,List,Optional

import stripe

from .constant import STRIPE_KEY

class StripeManager:

    @classmethod
    def set_api_key(self) -> None:
        stripe.api_key = STRIPE_KEY

class Customer:

    def __init__(self,**information:Optional[Dict[str,Any]]) -> None:
        
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

    def retrieve(self,user_id:str) -> stripe.Customer:

        return stripe.Customer.retrieve(user_id)


class FileAttach:

    def __init__(self,**information) -> None:
        
        self.__purpose:str = information["purpose"]
        self.__file = information["file"]
        self.__stripe_account:str = information["account"]

    @property
    def purpose(self) -> str:
        return self.__purpose
    
    @property
    def file(self):
        return self.__file
    
    @property
    def stripe_account(self) -> str:
        """

        Returns:
            str: stripe id returning
        """

        return self.__stripe_account
    
    def attach_new(self) -> Any:

        file_attaching_account = stripe.File.create(
            purpose = self.__purpose,
            file = self.__file,
            stripe_account = self.__stripe_account
        )

        individual:Dict[str,Any] = {
            "verification" : {
                "document" : {"front" : file_attaching_account.get("id"),},
                "additional_document" : {"front" : file_attaching_account.get("id")},
            }
        }

        stripe.Account.modify(self.__stripe_account,individual = individual)

    def new_source(self,user_id:str,token:str) -> Any:

        new_card_source:Any = stripe.Customer.create_source(user_id,source = token)

        return new_card_source

class SetupIntent:

    def __init__(self,**information) -> None:
        
        self.__payment_method_types:List[Any] = information["payment_method_types"]
        self.__customer = information["customer"]
        self.__describtion:str = information["describtion"]
        

    @property
    def payment_method_types(self) -> List[Any]:
        return self.__payment_method_types

    @property
    def customer(self):
        return self.__customer
    
    @property
    def describtion(self) -> str:
        return self.__describtion
    
    def new_setup(self):

        stripe.SetupIntent.create(
            payment_method_types = self.__payment_method_types,
            customer = self.__customer,
            describtion = self.__describtion
        )


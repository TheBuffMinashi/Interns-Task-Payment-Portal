from django.urls import path

from .views import NewCustomer

app_name:str = "stripe_payment"

urlpatterns = [
    path("new-customer",NewCustomer.as_view(),name="newcustomer"),
    
]
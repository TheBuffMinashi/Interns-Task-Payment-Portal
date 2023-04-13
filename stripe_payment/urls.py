from django.urls import path

from .views import NewCustomer,SetupIntent,PaymentIntent

app_name:str = "stripe_payment"

urlpatterns = [
    path("new-customer",NewCustomer.as_view(),name="newcustomer"),
    path("setup-intent",SetupIntent.as_view(),name="setupintent"),
    path("payment",PaymentIntent.as_view(),name="payment"),
]
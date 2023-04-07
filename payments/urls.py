from django.urls import path
from payments.views import PaymentView

urlpatterns = [
    path('payment', PaymentView.as_view(), name='payment')
    ]

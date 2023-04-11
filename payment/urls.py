from django.urls import path

from .views import CreatePaymentAPIView, ConfirmPaymentAPIView

urlpatterns = [
    path('', CreatePaymentAPIView.as_view(), name='create_payment'),
    path('webhook/', ConfirmPaymentAPIView.as_view(), name='confirm_payment'),
]

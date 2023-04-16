from django.urls import path
from paypal.standard.ipn.models import PayPalIPN
from .views import index, show_product, show_cart, checkout, process_payment, payment_done, payment_canceled
from django.views.decorators.csrf import csrf_exempt

app_name = "app"
urlpatterns = [
    path('', index, name='index'),
    path('product/<int:product_id>/<slug:product_slug>', show_product, name='product_detail'),
    path('cart/', show_cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('paypal-ipn/', csrf_exempt(PayPalIPN), name='paypal-ipn'),
    path('process-payment/', process_payment, name='process_payment'),
    path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_canceled, name='payment_cancelled'),
]

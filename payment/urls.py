from django.urls import path
from .views import CreateCheckoutSession

app_name = 'payment'

urlpatterns = [
    path('create-checkout-session/<int:pk>/', CreateCheckoutSession.as_view()),
]

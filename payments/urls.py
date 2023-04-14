from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('create/', views.PaymentCreateView.as_view(), name='create'),
    path('success/<str:token>/',
         views.ChangePaymentStatusView.as_view(), name='success'),
]

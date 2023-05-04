from django.urls import path
from . import views
from pay.views import GetAllPay,SearchPay
urlpatterns = [
 path("", views.index, name="index"),
 path("config/", views.pay_config, name="config"),
 path("pay/", views.pay_request, name="pay"),
 path("success/", views.success, name="success"),
 path("cancelled/", views.cancel, name="cancelled"),
 path('api/v1/get-all-pay/', GetAllPay.as_view(), name="get_all"),
 path('api/v1/search-pay/', SearchPay.as_view()),
]

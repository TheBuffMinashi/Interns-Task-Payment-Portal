from django.urls import path
from . import views
urlpatterns = [
 path("", views.index, name="index"),
 path("config/", views.pay_config, name="config"),
 path("pay/", views.pay_request, name="pay"),
 path("success/", views.success, name="success"),
 path("cancelled/", views.cancel, name="cancelled"),
]

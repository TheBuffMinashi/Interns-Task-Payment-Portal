from django.urls import path
from .views import (
    RegisterUser,
)

app_name = 'users'

urlpatterns = [
    path('register-user/', RegisterUser.as_view(), name='register-user'),
]

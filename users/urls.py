from django.urls import path
from .views import (
    RegisterUser, LoginUser,
)

app_name = 'users'

urlpatterns = [
    path('register-user/', RegisterUser.as_view(), name='register-user'),
    path('login-user/', LoginUser.as_view(), name='login-user'),
]

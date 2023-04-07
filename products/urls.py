from django.urls import path
from .views import (
    CreateProduct, ProductList, RetrieveUpdateDestroyProduct,
)

app_name = 'products'

urlpatterns = [
    path('create/', CreateProduct.as_view(), name='create-product'),
    path('list/', ProductList.as_view(), name='product-list'),
    path('list/<int:pk>/', RetrieveUpdateDestroyProduct.as_view(),
         name='retrieve-update-destroy-product'),
]

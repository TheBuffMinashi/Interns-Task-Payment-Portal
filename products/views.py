from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from .models import Product
from .serializers import (
    ProductSerializer,
)


class CreateProduct(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class RetrieveUpdateDestroyProduct(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

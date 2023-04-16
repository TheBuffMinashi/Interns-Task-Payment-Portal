from pay_module.models import Order, LineItem
from .serializers import LineItemSerializer

from rest_framework.viewsets import ModelViewSet

# Create your views here.


class CreateOrderViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = LineItem.objects.all()
    serializer_class = LineItemSerializer

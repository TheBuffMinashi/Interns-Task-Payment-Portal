from rest_framework import routers
from .views import CreateOrderViewSet


router = routers.DefaultRouter()
router.register('paypal/create/order', CreateOrderViewSet,basename='orders')
urlpatterns = router.urls

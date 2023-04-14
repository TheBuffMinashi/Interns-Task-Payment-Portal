from django.db import models
from common.models import BaseModel
from common.managers import ActiveManager
from django.contrib.auth import get_user_model
from products.models import Product
import uuid

User = get_user_model()


class Payment(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='payments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.FloatField(default=0)
    currency = models.CharField(max_length=3)
    quantity = models.IntegerField(default=0)
    paid = models.BooleanField(default=False)
    token = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def is_paid(self):
        return True if self.paid else False
    is_paid.boolean = True
    is_paid.short_description = 'Paid Status'

    def __str__(self):
        return f'{self.product} - {self.user}'

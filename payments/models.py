from django.db import models
from common.models import BaseModel
from common.managers import ActiveManager
from django.contrib.auth import get_user_model


User = get_user_model()


class Payment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency = models.CharField(max_length=3)
    content = models.TextField()
    stripe_charge_id = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
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
        return self.content

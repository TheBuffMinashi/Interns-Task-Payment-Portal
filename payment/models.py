from django.db import models
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = 'Pending', _('Pending')
        DONE = 'Done', _('Done')
        FAILED = 'Failed', _('Failed')

    status = models.CharField(choices=PaymentStatus.choices, default=PaymentStatus.PENDING, max_length=31)
    payment_id = models.CharField(max_length=127, null=True)
    amount = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=15, null=True)
    client_secret = models.CharField(max_length=255, null=True)

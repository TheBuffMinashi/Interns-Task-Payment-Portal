from django.db import models
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        REQUESTED = 'Requested', _('Requested')
        CREATED = 'Created', _('Created')
        DONE = 'Done', _('Done')
        FAILED = 'Failed', _('Failed')

    status = models.CharField(choices=PaymentStatus.choices, default=PaymentStatus.REQUESTED, max_length=31)
    payment_id = models.CharField(max_length=127, default='-')
    amount = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    currency = models.CharField(max_length=15, default='usd')
    client_secret = models.TextField(default='-')

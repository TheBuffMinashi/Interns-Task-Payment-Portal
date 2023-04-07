from django.db import models


class Payment(models.Model):
    amount = models.FloatField()
    currency = models.CharField(max_length=3)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_charge_id = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    payer_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.description

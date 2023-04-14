from django.db import models
from common.managers import ActiveManager
from common.models import BaseModel


class Product(BaseModel):
    CURRENCY_CHOICES = (
        ('USD', 'usd'),
        ('EUR', 'eur'),
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField(default=0)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3)
    image = models.ImageField(upload_to='products/images/')
    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

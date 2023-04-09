from django.db import models
from common.managers import ActiveManager
from common.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/images/')
    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

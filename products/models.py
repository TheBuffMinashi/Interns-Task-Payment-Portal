from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(
        verbose_name=_('Description'), null=True, blank=True)
    image = models.ImageField(
        upload_to='products/images/', verbose_name=_('Image'), null=True, blank=True)
    price = models.IntegerField(verbose_name=_('Price'), default=0)

    def __str__(self) -> str:
        return self.name

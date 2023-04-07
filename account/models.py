from django.db import models
from django.contrib.auth.models import User


class StripeInformation(models.Model):

    user = models.OneToOneField(
        User,on_delete=models.CASCADE,verbose_name="User"
    )

    stripe_id = models.CharField(max_length=50,
                                 verbose_name="Stripe Id",
                                 unique=True,
                                 blank=True,
                                 null=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} --- {self.stripe_id}"
    
    class Meta:
        verbose_name:str = "Stripe Information"
        verbose_name_plural:str = "Stripe Information"
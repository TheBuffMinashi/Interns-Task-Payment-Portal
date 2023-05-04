from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Payments(models.Model):
    Transaction = models.TextField(default=None)
    Amount = models.IntegerField(default=0)
    UserPay = models.ForeignKey("User", on_delete=models.CASCADE, related_name="Payuser")
    Time = models.DateTimeField(auto_now_add=True)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}- Transaction: {self.Transaction}, paid by {self.UserPay}"
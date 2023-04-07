from django.db import models

class Customer(models.Model):

    email = models.EmailField(
        max_length=150,verbose_name="Email"
    )

    describtion = models.TextField(
        max_length=500,verbose_name="Desc"
    )

    name = models.CharField(max_length=50,
                            verbose_name="Name")
    
    phone = models.CharField(max_length=15,
                             verbose_name="Phone")
    

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name_plural = "Customers"

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


class SetupIntent(models.Model):

    from_customer = models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name="From Customer",related_name="from_customers_setupintent")
    to_customer = models.ForeignKey(Customer,on_delete=models.CASCADE,verbose_name="To Customer",related_name="to_customers_setupintent")

    desc = models.TextField(verbose_name="Describtion")

    def __str__(self) -> str:
        return self.from_customer.name + " " + self.to_customer.name
    
    class Meta:
        verbose_name_plural = "SetupIntent"
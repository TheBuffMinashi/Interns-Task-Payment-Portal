from django.contrib import admin
from .models import Product, PaymentHistory

admin.site.register(Product)
admin.site.register(PaymentHistory)
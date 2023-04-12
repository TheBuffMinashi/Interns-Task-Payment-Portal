from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_id', 'amount', 'status', 'client_secret', 'date_created', 'date_modified')

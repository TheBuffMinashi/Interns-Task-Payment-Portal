from django.contrib import admin

from .models import Customer,SetupIntent


class CustomerAdmin(admin.ModelAdmin):
    ...

admin.site.register(Customer,CustomerAdmin)

class SetupIntentAdmin(admin.ModelAdmin):
    ...

admin.site.register(SetupIntent,SetupIntentAdmin)

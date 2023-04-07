from django.contrib import admin

from .models import StripeInformation


class StripeInformationAdmin(admin.ModelAdmin):
    ...

admin.site.register(StripeInformation,StripeInformationAdmin)

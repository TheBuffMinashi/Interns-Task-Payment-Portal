# Generated by Django 4.2 on 2023-04-12 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_remove_payment_client_secret_payment_checkout_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='checkout_url',
            new_name='client_secret',
        ),
    ]

# Generated by Django 4.2 on 2023-04-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]

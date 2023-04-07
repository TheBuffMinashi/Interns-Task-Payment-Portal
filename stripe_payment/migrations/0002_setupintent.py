# Generated by Django 4.2 on 2023-04-07 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetupIntent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(verbose_name='Describtion')),
                ('from_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_customers_setupintent', to='stripe_payment.customer', verbose_name='From Customer')),
                ('to_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_customers_setupintent', to='stripe_payment.customer', verbose_name='To Customer')),
            ],
            options={
                'verbose_name_plural': 'SetupIntent',
            },
        ),
    ]

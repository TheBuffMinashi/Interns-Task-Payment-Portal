# Generated by Django 4.2 on 2023-04-06 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(max_length=3)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('payer_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_bought',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210409_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

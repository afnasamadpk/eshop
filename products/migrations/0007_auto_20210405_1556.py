# Generated by Django 3.1.7 on 2021-04-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]

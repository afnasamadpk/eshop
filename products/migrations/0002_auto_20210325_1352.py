# Generated by Django 3.1.7 on 2021-03-25 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='review',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='review',
            name='rate',
        ),
    ]

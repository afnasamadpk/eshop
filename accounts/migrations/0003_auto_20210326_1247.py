# Generated by Django 3.1.7 on 2021-03-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccounts_shortname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepicture',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
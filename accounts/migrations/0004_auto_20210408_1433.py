# Generated by Django 3.1.7 on 2021-04-08 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210326_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccounts',
            name='shortname',
            field=models.CharField(max_length=12, verbose_name='name'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('country', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('phone', models.IntegerField()),
                ('pincode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
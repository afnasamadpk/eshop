from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import UserAccounts
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length = 60)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    added_date=models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name




class Review(models.Model):
    user = models.ForeignKey(UserAccounts,on_delete=models.CASCADE,related_name='review')
    products = models.ForeignKey(Products,on_delete=models.CASCADE)
    subject = models.CharField(max_length = 80)
    added_date=models.DateTimeField(auto_now_add = True)
    update_date=models.DateTimeField(auto_now = True)
    comment = models.TextField( max_length = 150)

    def __str__(self):
        return self.subject

# class Rating(models.Model):
#     rate = models.IntegerField(default = 0)

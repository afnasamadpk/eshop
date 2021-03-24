from django.db import models
from products.models import Products
from accounts.models import UserAccounts

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete = models.CASCADE,related_name = 'product')
    user = models.ForeignKey(UserAccounts,on_delete = models.CASCADE,related_name = 'cart_items')
    def __str__(self):
        return self.product.name

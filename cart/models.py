from django.db import models
from products.models import Products
from accounts.models import UserAccounts

class Cart(models.Model):
    id = models.BigAutoField(primary_key = True)
    product = models.ForeignKey(Products,on_delete = models.CASCADE,related_name = 'product')
    user = models.ForeignKey(UserAccounts,on_delete = models.CASCADE,related_name = 'cart_items')
    def __str__(self):
        return self.product.name


class Wishlist(models.Model):
    id = models.BigAutoField(primary_key = True)
    product = models.ForeignKey(Products,on_delete = models.CASCADE,related_name = 'items')
    user = models.ForeignKey(UserAccounts,on_delete = models.CASCADE,related_name = 'wish_list')
    def __str__(self):
        return self.product.name

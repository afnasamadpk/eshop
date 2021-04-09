from django.db import models
from products.models import Products
from accounts.models import UserAccounts


class Cart(models.Model):
    id = models.BigAutoField(primary_key = True)
    product = models.ForeignKey(Products,on_delete = models.CASCADE,related_name = 'product')
    user = models.ForeignKey(UserAccounts,on_delete = models.CASCADE,related_name = 'cart_items')
    quantity=models.PositiveIntegerField(default=1)
    is_bought = models.BooleanField(default = False)

    def __str__(self):
        return self.product.name

    def sub_total(self):
        sub_total = self.product.price * self.quantity
        print(sub_total)
        return sub_total



class Wishlist(models.Model):
    id = models.BigAutoField(primary_key = True)
    product = models.ForeignKey(Products,on_delete = models.CASCADE,related_name = 'items')
    user = models.ForeignKey(UserAccounts,on_delete = models.CASCADE,related_name = 'wish_list')
    
    def __str__(self):
        return self.product.name


class Checkout(models.Model):
    id = models.BigAutoField(primary_key = True)
    user = models.ForeignKey(UserAccounts,on_delete=models.CASCADE,related_name='checkout')
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart')
    bill_id = models.BigIntegerField()
    price = models.PositiveIntegerField()

    

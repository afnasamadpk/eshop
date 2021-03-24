from django.shortcuts import render,redirect,HttpResponse

from cart.models import Cart
from products.models import Products
from accounts.models import UserAccounts
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash



# Create your views here.
@login_required(login_url="/login/")
def add_to_cart(request,id):

    next = request.GET.get('next', '/')
    product = Products.objects.get(id = id)
    user = request.user
    
    p = Cart(user=user,product=product)
    p.save()
    return redirect(next)

    # c = Cart.objects.filter(user=user)
    # return HttpResponse(str(len(c)))


def view_cart(request):
    return render(request,'cart/cart-page.html')

def remove_from_cart(request,id):
    next = request.GET.get('next', '/')

    item = Cart.objects.get(id = id)
    item.delete()

    return redirect(next)
    








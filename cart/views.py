from django.shortcuts import render,redirect,HttpResponse
from cart.models import Cart,Wishlist,Checkout
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

@login_required(login_url="/login/")
def view_cart(request):
    
    return render(request,'cart/cart-page.html')


def remove_from_cart(request,id):
    next = request.GET.get('next', '/')
    item = Cart.objects.get(id = id)
    item.delete()
    return redirect(next)
    

def wish_list(request,id):
    next = request.GET.get('next', '/')
    product = Products.objects.get(id = id)
    user = request.user 
    p = Wishlist(user=user,product=product)
    p.save()
    return redirect(next)


def view_wishlist(request):
    wish_list = []
    if request.user.is_authenticated:
         wish_list=Wishlist.objects.filter(user = request.user)
    return render(request,'cart/wishlist.html',{'wish_list':wish_list})
      
    
def cart_add(request,id):
    product=Cart.objects.get(id=id)
    product.quantity = product.quantity + 1
    product.save()
    # print(product.quantity)
    return redirect('/cart/')


def cart_sub(request,id):
    product=Cart.objects.get(id=id)
    
    if product.quantity != 1:

        product.quantity = product.quantity - 1
        product.save()
    print(product.quantity)
    return redirect('/cart/')

def checkout(request):
    user = request.user
    cart = Cart.objects.filter(user = user,is_bought=False)
    bill_id = Checkout.objects.all().latest('bill_id').bill_id
    bill_id = bill_id + 1
    for c in cart:   
        checkout = Checkout(user=user,cart=c, price=c.product.price,bill_id=bill_id)
        checkout.save()
        c.product.quantity = c.product.quantity - c.quantity 
        c.product.save()
        c.is_bought = True
        c.save()

    return redirect('home')













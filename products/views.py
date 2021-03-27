from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from products.models import Products,Category,Rating
from products.forms import ReviewModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
# def show_one_product(request,id):
#     p = Products.objects.get(id=id)
#     # reviews = p.review_set.all()

#     return render(request,'products/product-details-3.html',{'p':p})
  
@login_required(login_url="/login/")
def show_one_product(request,id):
    p = Products.objects.get(id = id)
    reviews = p.review_set.all()
    if request.method == 'POST':
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.products = p
            obj.user = request.user
            obj.save()
            # return HttpResponse('added')
            return redirect(f'/product/{id}/')
        else:
            return render (request,'products/product-details-3.html',{'form':form})

    else:
        product = Products.objects.get(id = id)
        rate = Rating.objects.filter(user=request.user,product=product).first()
        five_stars = [1,2,3,4,5]
        rating = 0
        if rate:
            rating = rate.rate

        form = ReviewModelForm()
        return render (request,'products/product-details-3.html',{'form':form,'p':p,'reviews':reviews, 'rating': rating, 'five_stars':five_stars})


def show_products(request,id):
    category = Category.objects.get(id = id)
    products = category.products_set.all()
    return render(request,'products/shop.html',{'products':products})


def rating(request, product_id, rating):
    
    next = request.GET.get('next', '/')
    product = Products.objects.get(id = product_id)
    user = request.user
    rate = Rating.objects.filter(user=user,product=product).first()
    if rate:
        rate.rate = rating
        rate.save()
    else:
        Rating.objects.create(user=user,product=product, rate=rating)
        
    count = Rating.objects.filter(product=product)
    return redirect(next)
    

# def show_reviews(request,id):
#     p = Products.objects.get(id = id)
#     reviews = p.review_set.all()
#     return render (request,'products/product-details-3.html',{'p':p,'reviews':reviews})
    
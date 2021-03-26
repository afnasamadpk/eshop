from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from products.models import Products,Category
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
        form = ReviewModelForm()
        return render (request,'products/product-details-3.html',{'form':form,'p':p,'reviews':reviews})


def show_products(request,id):
    category = Category.objects.get(id = id)
    products = category.products_set.all()
    return render(request,'products/shop.html',{'products':products})


# def rating(request,id):
    



# def show_reviews(request,id):
#     p = Products.objects.get(id = id)
#     reviews = p.review_set.all()
#     return render (request,'products/product-details-3.html',{'p':p,'reviews':reviews})
    
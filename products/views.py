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
        context = {'form':form,'p':p,'reviews':reviews, 'rating': rating, 'five_stars':five_stars}
        return render (request,'products/product-details-3.html',context)


def show_products(request,category_id):
    category = Category.objects.get(id = category_id)
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
        
    
    # print(count)
    return redirect(next)
    # return redirect(next)
    
# def show_rating(request,id):
#     count = Rating.objects.filter(product=product)
#     star_count =str(len(count))
#     sum=0
#     for i in count:
#         # print(i.rate)
#         sum +=i.rate
#     print(star_count)
#     print(int(sum)/int(star_count))

#     rated_value = int(sum)/int(star_count)
#     return render(request,'product-details-3.html',{'rated_value':rated_value})




# def show_reviews(request,id):
#     p = Products.objects.get(id = id)
#     reviews = p.review_set.all()
#     return render (request,'products/product-details-3.html',{'p':p,'reviews':reviews})
    
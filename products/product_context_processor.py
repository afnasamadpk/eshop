from products.models import Category,Products

def category(request):

    
    category=Category.objects.all()

    return {
            

        'category': category

    }
def products(request):

    
    products=Products.objects.all()

    return {
            

        'products': products

    }




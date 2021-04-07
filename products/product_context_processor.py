from products.models import Category,Products

def category(request):
   
    category=Category.objects.all()

    return {
            

        'category': category

    }






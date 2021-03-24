from cart.models import Cart

def cart_items(request):
    cart_items = []
    if request.user.is_authenticated:
        cart_items=Cart.objects.filter(user = request.user)

    return {
        

        'cart_items': cart_items

    }




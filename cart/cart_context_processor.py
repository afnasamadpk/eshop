from cart.models import Cart

def cart_items(request):
    cart_items = []
    if request.user.is_authenticated:
        cart_items=Cart.objects.filter(user = request.user,is_bought=False)
        print(len(cart_items))
        
        s = 0
        for i in cart_items:
            s += i.quantity*i.product.price

    return {
        

        'cart_items': cart_items,
        's':s

    }



def cart_count(request):
    if request.user.is_authenticated:
        count = Cart.objects.filter(user = request.user,is_bought=False).count()
        return {'cart_count': count}
    return {'cart_count': 0}

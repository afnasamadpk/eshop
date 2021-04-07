
from django.urls import path
from cart.views import add_to_cart,view_cart,remove_from_cart,wish_list,view_wishlist,cart_add,cart_sub

urlpatterns = [
    path('cart/create/<int:id>/',add_to_cart,name='add_to_cart'),
    path('cart/',view_cart,name='view_cart'),
    path('cart/delete/<int:id>/',remove_from_cart,name='remove_from_cart'),
    path('wishlist/<int:id>/',wish_list,name='wish_list'),
    path('viewwishlist/',view_wishlist,name='view_wishlist'),
    path('cartadd/<int:id>/',cart_add,name='cart_add'),
    path('cartminus/<int:id>/',cart_sub,name='cart_sub'),

]

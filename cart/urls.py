
from django.urls import path
from cart.views import add_to_cart,view_cart,remove_from_cart

urlpatterns = [
    path('addtocart/<int:id>/',add_to_cart,name='add_to_cart'),
    path('viewcart/',view_cart,name='view_cart'),
    path('removefromcart/<int:id>/',remove_from_cart,name='remove_from_cart')
]

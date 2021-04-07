"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from products.views import show_one_product,show_products,rating,show_categorywise

urlpatterns = [
    path('products/<int:id>/',show_one_product,name='show_one_product'),
    path('products/',show_products,name='show_products'),
    path('rating/<int:product_id>/<int:rating>/',rating,name='rating'),
    path('showcategorywise/<int:category_id>/',show_categorywise,name='show_categorywise')
    # path('showreviews/<int:id>/',show_reviews,name='show_reviews')
    # path('review/<int:id>/',review,name = 'review'),
    
]


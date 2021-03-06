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
from accounts.views import home,register,log_in,log_out,my_account,add_address,view_address

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    path('editaccountdetails/',my_account,name='my_account'),
    path('addaddress/',add_address,name='add_address'),
    path('viewaddress/',view_address,name = 'view_address')
    # path('edituser/<int:id>/',edit_user,name='edit_user')
    


    # path('login/',home,name='home'),
]

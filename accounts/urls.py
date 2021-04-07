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
from accounts.views import home,register,log_in,log_out,change_password

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',log_in,name='log_in'),
    path('logout/',log_out,name='log_out'),
    path('changepassword/',change_password,name='change_password'),
    


    # path('login/',home,name='home'),
]

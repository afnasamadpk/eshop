from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from accounts.forms import RegistrationForm,EditForm,AddressForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import AbstractUser
from accounts.models import Address
from django.contrib.auth.decorators import login_required

# class Home(TemplateView):
#     template_name = 'accounts/index.html'

def home(request):
    return render(request,'accounts/index.html')


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'accounts/register.html',{'form':form})

    else:
        form = RegistrationForm()
        return render(request,'accounts/register.html',{'form':form})


def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('email or password is incorrect')

    return render(request,'accounts/login.html')

def log_out(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url="/login/")
def my_account(request):
    user = request.user  
    if request.method =='POST':
        form = PasswordChangeForm(data = request.POST,user=request.user)
        form1 = EditForm(request.POST,instance=user)

        if form.is_valid():
            obj = form.save()
            if form1.is_valid():
                obj1 = form1.save(commit=False)
                obj1.user = obj
                obj1.save()
                update_session_auth_hash(request,form.user)
            return redirect('home')
        else:
            return render(request,'accounts/my-account.html',{'form':form,'form1':form1})

    else:
        form = PasswordChangeForm(user=request.user)
        form1 = EditForm(instance=user)
        return render(request,'accounts/my-account.html',{'form':form,'form1':form1})


def add_address(request):
    
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
        else:
            return render(request,'accounts/checkout.html',{'form':form})

    else:
        form = AddressForm()
        return render(request,'accounts/checkout.html',{'form':form})


def view_address(request):
    user = request.user
    address = Address.objects.filter(user = user)
    return render (request,'accounts/my-account.html',{'address':address})
    

# def edit_user(request,id):
#     user = request.user  
#     if request.method =='POST':
#         form1 = EditForm(request.POST,instance=user)
#         if form1.is_valid():
#             form1.save()
#             return redirect('home')
#         else:
#             return render(request,'accounts/my-account.html',{'form1':form1})

#     else:
#         form1 = EditForm(instance=user)
#         return render(request,'accounts/my-account.html',{'form1':form1})
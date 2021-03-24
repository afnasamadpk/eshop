from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.views.generic import ListView,DetailView,TemplateView,CreateView
from accounts.forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash



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
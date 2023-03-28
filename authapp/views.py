from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        print(get_email)
        print(get_password)
        print(get_confirm_password)
        if get_password!=get_confirm_password:
            messages.info(request,'passwords do not match')
            return redirect('/auth/signup')
        try:
            if User.objects.get(username=get_email):
                messages.warning(request, 'Email is Taken')
                return redirect('/auth/signup')
        except Exception as identiifier:
            pass
        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()
        messages.success(request,"User is Created please login")
        return redirect('/auth/login/')

    return render(request,'signup.html')

def handleLogin(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        myuser=authenticate(username=get_email, password=get_password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login success") 
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials')

    return render(request,'login.html')
def handleLogout(request):
    logout(request)
    messages.success(request, 'log out success')
    return render(request,'login.html')
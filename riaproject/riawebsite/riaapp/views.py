from django.shortcuts import render,redirect
from django.contrib import messages
import re

# Create your views here.
def index(request):
    return render(request,"home.html")
def handleSignin(request):
    if request.method=="POST":
        flag= 0
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return redirect('/signin')
        if len(password) <= 8:
            messages.warning(request, "password must be atleast 8 charecters")
            return redirect('/signin')
            

        messages.info(request,f"{name},{email},{password},{confirm_password}")
    return render(request,"signin.html")

def handleLogin(request):
    return render(request,"login.html")
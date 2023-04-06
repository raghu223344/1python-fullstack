from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"home.html")
def handlesignin(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signin.html')
        messages.info(request,f"{name},{email},{password},{confirm_password}")
    return render(request,"signin.html")

def handlelogin(request):
    return render(request,"login.html")
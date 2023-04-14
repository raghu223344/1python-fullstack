from django.urls import path
from riaapp import views

urlpatterns = [
    
    path('',views.index,name="index"),
   path('signin',views.handleSignin,name="handleSignin"), 
   path('login',views.handleLogin,name="handleLogin"), 
]
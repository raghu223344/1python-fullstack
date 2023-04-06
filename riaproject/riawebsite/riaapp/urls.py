from django.urls import path
from riaapp import views

urlpatterns = [
    
    path('',views.index,name="index"),
   path('signin',views.handlesignin,name="handlesignin"), 
   path('login',views.handlelogin,name="handlelogin"), 
]
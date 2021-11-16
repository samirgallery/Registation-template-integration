from django.core.checks import messages
from django.shortcuts import render
from.models import*
# Create your views here.

#vies for register page 
def RegisterPage(request):
    return render(request,"app/register.html")

#View for user registation 
def UserRegister(request):
    if request.method =="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']


        #first we will validate that user alrady exsit
        user=User.objects.filter(Email=email)
        

        if user:
            messages ="user all ready exits "
            return render (request,"app/register.html",{'msg':messages})
        
        else:
            if password == cpassword:
                newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                messages="User register samir page Successfully "
                return render(request,"app/login.html",{'msg':messages})
            else:
                messages="password and confirm password does not match "
                return render (request,"app /register.html",{'msg':messages})

        
    


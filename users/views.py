from choices.models import Choice
from django.contrib import messages
from django.http import Http404,HttpResponse
from django.shortcuts import render,redirect
from users.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register_user(request):
    form= RegistrationForm()
    if request.method == 'POST':
        form= RegistrationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.save()
            login(request,user)
            return redirect("questions:home")
        else:
            messages.error(request,"Error: Unable to register user")
    context= {"form":form}
    return render(request,"users/register.html",context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect("questions:home")
    else:
        form= LoginForm()
        if request.method == "POST":
            form= LoginForm(request.POST)
            if form.is_valid():
                username= form.cleaned_data["username"]
                password= form.cleaned_data["password"]
                user= authenticate(username=username,password=password)

                if user is not None:
                    login(request,user)
                    return redirect("questions:home")
                else:
                    messages.error(request,"Error: User with given credentials not found")
            else:
                messages.error(request,"Error: Unable to login user")
        context= {"form":form}
        return render(request,"users/login.html",context)

@login_required(login_url="authentication:login-user")
def votes(request):
    choices= request.user.votes.all()
    context= {"choices":choices}
    return render(request,"users/votes.html",context)

@login_required(login_url="questions:home")
def logout_user(request):
    logout(request)
    return redirect("questions:home")
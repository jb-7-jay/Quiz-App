from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from csv import writer

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,"users/register.html",{'form':form})


# there no need of making function for login and logout because we use class based Loginview and Logout 

# def login(request):
#     return render(request,"login.html")

@login_required
def profile(request):
    return render(request,"users/profile.html")
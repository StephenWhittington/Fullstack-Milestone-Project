from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')
    
def logout(request):
    """logs the user out"""
    auth.logout(request)
    messages.success(request, "you have successfully been loged out!")
    return redirect(reverse('index'))
    
def login(request):
    """returns a login page"""
    login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})

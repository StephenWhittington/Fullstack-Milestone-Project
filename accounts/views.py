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
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            messages.success(request, "You have successfully loged in!")

            if user:
                auth.login(user=user, request=request)
            else:
                login_form.add_error(None, "Your username or password is Incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})

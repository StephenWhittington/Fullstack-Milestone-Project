from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib import auth, messages
from django.core.urlresolvers import reverse, reverse_lazy
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm

def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')

@login_required   
def logout(request):
    """logs the user out"""
    auth.logout(request)
    messages.success(request, "you have successfully been loged out!")
    return redirect(reverse('index'))
    
def login(request):
    """returns a login page and redirects the user to the home page
    after they log in"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)

def registration(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'registration.html', args)

@login_required
def customer(request):
    """A view that displays the customer page of a logged in user"""
    user_id = request.user.pk 
    currentcustomer = Customer.objects.get(user=user_id)
    return render(request, 'customer.html', {'customer': currentcustomer})

@login_required
def create_or_edit_customer(request, pk=None):
    """
    Create's a view that allows us to create
    or edit a customer depending if the Post ID
    is null or not
    """
    details = get_object_or_404(Customer, pk=pk) if pk else None
    if request.method == "POST":
        customer = CustomerForm(request.POST, request.FILES, instance=details)
        if customer.is_valid():
            details = customer.save()
            return redirect(customer, customer.pk)
    else:
        customer = CustomerForm(instance=details)
    return render(request, 'edit_customer.html', {'customer': customer})

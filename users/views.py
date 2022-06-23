from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .helpers import auth_user_should_not_access
from django.contrib.auth import logout

# Create your views here.

@auth_user_should_not_access
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account for {username} has been created successfully')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'users/register_optional.html', context)


@auth_user_should_not_access
def login(request):
    form = UserLoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/') 
        else:
            msg = 'error validating form'

    return render(request, 'users/login1.html', {'form': form, 'msg': msg})

# def logout_view(request):
#     logout(request)
#     return redirect('home')
    

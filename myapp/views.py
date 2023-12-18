from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegister
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login

from django.contrib.auth.forms import AuthenticationForm  # Import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}")
            return redirect('login')

    else:
        form = UserRegister()
    return render(request,'myapp/register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login (request, user)
                # Redirect to a success page or home page after login
                return redirect('profile')  # Replace 'home' with your URL name
            else:
                messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    # Redirect to a success page or home page after logout
    return render(request,'myapp/logout.html')


@login_required
def profile(request):
    return render(request, 'myapp/profile.html')
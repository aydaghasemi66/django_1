from django.shortcuts import render, redirect
from allauth.account.forms import SignupForm, LoginForm
from allauth.account.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def account_signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(request)
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid')
    else:
        form = SignupForm()

    return render(request, 'account/signup.html', {'form': form})

def account_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')  # Use 'login' field for username
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

def account_logout(request):
    logout(request)
    return redirect('/')

def change_email(request):
    return render(request, 'account/change_email.html')

def password_reset(request):
    if request.method == 'POST':
        messages.success(request, "Password reset email sent successfully.")
        return PasswordResetView.as_view()(request)
    return render(request, 'account/password_reset_form.html')

def password_reset_done(request):
    return render(request, 'account/password_reset_done.html')

def change_password(request):
    return render(request, 'account/password_change.html')
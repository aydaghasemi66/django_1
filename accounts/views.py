
from allauth.account.views import LoginView, SignupView ,LogoutView
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def account_signup(request):
    if request.method == 'POST':
        messages.success(request, "you signed up sucsessfully")
        return redirect('home') 

    return render(request, 'account/signup.html') 


def account_login(request):
    if request.method == 'POST':

        messages.success(request, "you logged in sucsessfully")
        return redirect('home') 

    return render(request, 'account/login.html')  

#
def accouont_logout(request):
   
    messages.success(request, "you logged out sucsessfully")
    return LogoutView.as_view()(request) 


@login_required
def change_email(request):

    return render(request, 'account/change_email.html')
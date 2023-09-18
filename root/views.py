from django.shortcuts import render , redirect
from .models import Services, NewsLetter
from courses.models import Course,Trainer
from courses.models import Category
from django.contrib.auth.models import User
from .forms import NewsLetterForm, ContactUsForm
from django.contrib import messages

# Create your views here.



def home (request):
    if request.method == 'GET':
        service_count = Services.objects.filter(status=True).count()
        course_count = Course.objects.filter(status=True).count()
        trainer_count = Trainer.objects.filter(status=True).count()
        user_count = User.objects.filter(is_active=True).count()
        category = Category.objects.all()   

        services = Services.objects.filter(status=True)
        last_three_course = Course.objects.filter(status=True)[:3]
        last_three_trainer = Trainer.objects.filter(status=True)[:3]
        context = {
            'service':services,
            'course':last_three_course,
            'trainer':last_three_trainer,
            'category':category,
            'sc' : service_count,
            'cc' : course_count,
            'tc' : trainer_count,
            'uc' : user_count,
        }
        return render(request,"root/index.html" , context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:home')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:home')
        

def about (request):
    if request.method == 'GET' :
        category = Category.objects.all()
        context = {
            'category':category,
        }
        return render(request,"root/about.html",context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:about')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:about')

def contact(request):
    if request.method =='GET':
        category = Category.objects.all()
        context = {
            'category':category,
        }
        return render(request,"root/contact.html",context=context)
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:contact')
        
    elif request.method == 'POST' and len(request.POST) > 2 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you you as soon')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')   
    


def trainer(request):
    if request.method =='GET':
        category = Category.objects.all()
        trainer = Trainer.objects.filter(status=True)
        context = {
            'category':category,
            'trainer':trainer,
        }
        return render(request,"root/trainers.html",context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:trainer')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:trainer')
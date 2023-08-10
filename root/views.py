from django.shortcuts import render
from .models import Services




def home(request):
    services = Services.objects.all()
    context = {
        'service':services
    }
    return render(request,"root/index.html",context=context)



def about (request):
    context = {
      
    }
    return render(request,"root/about.html", context=context)


def contact(request):
    context = {
     
    }
    return render(request,"root/contact.html", context=context)



def trainer(request):
    context = {
    
    }
    return render(request,"root/trainers.html", context=context)

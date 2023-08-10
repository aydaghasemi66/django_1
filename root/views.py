from django.shortcuts import render
from .models import Services




def home(request):
    services = Services.objects.all()
    context = {
        'service':services
    }
    return render(request,"root/index.html",context=context)



def about(request):
    return render(request,"root/about.html")

def contact(request):
    return render(request,"root/contact.html")

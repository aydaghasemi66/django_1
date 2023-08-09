from django.shortcuts import render




def home(request):
    return render(request,"root/index.html")

def about(request):
    return render(request,"root/about.html")

def contact(request):
    return render(request,"root/contact.html")





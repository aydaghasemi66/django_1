from django.shortcuts import render
from .models import Course

# Create your views here.


def courses(request):
    course = Course.objects.all()

    context = {
        'courses':course
    }
    return render(request,'courses/course.html')
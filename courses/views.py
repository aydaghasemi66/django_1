from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Course
from courses.models import Category

def courses(request, cat=None, teacher=None):
    category = Category.objects.all()
    
    if cat:
        course_list = Course.objects.filter(category__name=cat)
    elif teacher:
        course_list = Course.objects.filter(teacher__info__username=teacher)
    else:
        course_list = Course.objects.filter(status=True)
    
    paginator = Paginator(course_list, 2)  
    page_number = request.GET.get('page')
    courses = paginator.get_page(page_number)
    
    context = {
        "courses": courses,
        'category': category,
    }
    return render(request, 'courses/course.html', context=context)

                          

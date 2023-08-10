from django.contrib import admin
from .models import *

admin.site.register(Services)
class AdminServices(admin.ModelAdmin):
    list_display = ['title','content','status']
    list_filter = ['status']
    search_fields = ['title']
# Register your models here.


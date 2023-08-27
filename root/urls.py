from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path("",home,name="home"),# type: ignore
    path("about",about,name="about"),# type: ignore
    path("contact",contact,name="contact"), # type: ignore
    path("trainer",trainer,name="trainer")
]
from . import views
from django.urls import path
from core import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('service/',views.service,name="service"),
    path('contact/',views.contact,name="contact"),
    path('members/',views.members,name="members"),

    
]

from django.urls import is_valid_path
from .models import Member, Contacts
from .forms import Contactforms,MemberRegistrationForm
from django.shortcuts import render

def index(request):  
    return render(request,"index.html")




def about(request):  
    return render(request,"about.html")


def service(request):  
    return render(request,"service.html")


def contact(request):
    form = Contactforms()
    if (request.method=="POST"):
        form = Contactforms(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            name=cd.get('name')
            email=cd.get('email')
            contact=Contacts.objects.create(name=name, email=email)

    #if (request.method=="POST"):
       # name=request.POST.get("name")
       # message=request.POST.get("message")
       # email=request.POST.get("email")
       # print(name,message)
    return render(request,"contact.html", {'form':form})

def members(request):
    form=MemberRegistrationForm()
    members=Member.objects.filter(is_active=True)
    return render(request,"members.html",{'members':members, "form": form})

    
# Create your views here.

from email import message
from pyexpat import model
from re import T
from django.db import models

# Create your models here.
POSITION_CHOICES=(
    ('member','member'),
    ('developer','developer'),
    ('instructor','instructor')
)

class Member(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30,unique=True)
    bio=models.TextField(blank=True,null=True)
    position=models.CharField(max_length=50,choices=POSITION_CHOICES)
    is_active=models.BooleanField(default=True)

class Contacts(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.TextField(blank=True, null=True)
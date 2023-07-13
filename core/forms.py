import email
from email import message
from statistics import mode
from types import MemberDescriptorType
from django import forms
from django import forms

from core.models import Member
class Contactforms(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    message=forms.Textarea()

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model= Member()
        fields=("fname","lname","email","bio")
        
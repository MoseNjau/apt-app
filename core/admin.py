from django.contrib import admin

from core.forms import Contactforms
from .models import Member
from .models import Contacts
# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=['fname','lname','email','position','is_active']
    list_filter=['is_active','position']


    @admin.register(Contacts)
    class ContactAdmin(admin.ModelAdmin):
        list_display= ['name','email']
        list_filter=['name']
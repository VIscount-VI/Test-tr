from django.contrib import admin
from .models import Name
# Register your models here.




class Admin_Name(admin.ModelAdmin):



    list = ['first_name',  'last_name']



admin.site.register(Name, Admin_Name)
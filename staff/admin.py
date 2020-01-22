from django.contrib import admin
from .models import Staff,Staff_Group


# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['display_name','Gender','dob','contact_no',]
    list_filter =('display_name','Gender', 'dob',)
    
 

@admin.register(Staff_Group)
class Staff_GroupAdmin(admin.ModelAdmin):
    list_display = ['name','activity','lvl',]
    list_filter =('name','activity','lvl',)

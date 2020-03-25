from django.contrib import admin
from .models import Staff,Staff_Group


# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['display_name','gender','dob','contact_no','get_image_url']
    list_filter =('display_name','gender', 'dob',)
    
 

@admin.register(Staff_Group)
class Staff_GroupAdmin(admin.ModelAdmin):
    list_display = ['name','is_active','lvl',]
    list_filter =('name','is_active','lvl',)

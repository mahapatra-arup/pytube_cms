from django.contrib import admin
from .models import Org_Details

# Register your models here.
@admin.register(Org_Details)
class Org_DetailsAdmin(admin.ModelAdmin):
   

#
    list_display = ["org_Name","org_code","dist","updated_on"]
    list_display_links = ["org_Name","org_code"]

    #Stop Delete
    def has_delete_permission(self, request, obj=None):
        return False

      




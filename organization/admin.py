from django.contrib import admin
from .models import Org_Details,Org_SocialDetails,Org_ContactNo,Org_UsefulLinks

# Register your models here.
@admin.register(Org_Details)
class Org_DetailsAdmin(admin.ModelAdmin):

    #
    list_display = ["org_name","org_code","dist","updated_on"]
    list_display_links = ["org_name","org_code"]

    #if atlist one row exist then add button not work/hide
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Org_Details.objects.exists():
            retVal = False
        return retVal

    #Stop Delete
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Org_SocialDetails)
class Org_SocialDetailsAdmin(admin.ModelAdmin):
    pass    

@admin.register(Org_ContactNo)
class Org_ContactNoAdmin(admin.ModelAdmin):
    pass   

@admin.register(Org_UsefulLinks)
class Org_UsefulLinksAdmin(admin.ModelAdmin):
    pass  





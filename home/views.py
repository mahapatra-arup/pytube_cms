from django.shortcuts import render
from django.views.generic import TemplateView
from pytube.settings import base,development
from django.http import HttpResponseRedirect
from  organization.models import Org_Details
# Redirect to home Index
def Index_Redirect(request):
    return HttpResponseRedirect("index")

# Create your Home Index
class IndexView(TemplateView):
    template_name = "home/index.html"
    
     #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        # //get dada
        orgDetails = Org_Details.objects.all().first()
        if orgDetails:
            context.update({
            "description": orgDetails.org_name+', '+orgDetails.at+', '+orgDetails.po+', '+orgDetails.ps+', '+orgDetails.dist+', '+orgDetails.org_code+', '+orgDetails.email+', '+orgDetails.website,
            "title": orgDetails.org_name,
            "keywords": orgDetails.org_name+', '+orgDetails.at+', '+orgDetails.po+', '+orgDetails.ps+', '+orgDetails.dist+', '+orgDetails.org_code+', '+orgDetails.email+', '+orgDetails.website,
            "author": orgDetails.org_name,
            "page_title":'Welcome to '+orgDetails.org_name,
        })
           
        else:
           context.update({
            "description": 'Home',
            "title": 'Home',
            "keywords": 'Home',
            "author": "Pytube",
            "page_title":'Welcome to ',
        })
       
       
        
        return context
    
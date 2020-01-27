from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Staff_Group
from pytube.settings import base,development

# Create your views here.
#<===================,user__is_active=True,user__is_staff=True
#Staff List==
class StaffListView(ListView):
     #fixed
    template_name = "staff/staff_list.html"
    queryset = Staff_Group.objects.filter(is_active=True).order_by('-lvl')
    context_object_name = "ds_staff_group"
    
    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Staff',
            "title": 'Staff',
            "keywords": 'Staff',
            "author": development.BLOG_AUTHOR,
            "page_title":'Staff',
        })
        return context
#===============>

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Staff_Group
from pytube.settings import base,development
from django.shortcuts import  get_object_or_404, render
from page.models import Menu  # menu Import

# Create your views here.
#<===================,
#Staff List==
class StaffListView(ListView):
    #Custom var
    name_of_slug="menu_slug"#only use title name not staff filter beacause staff template only one


     #fixed
    template_name = "staff/staff_list.html"
    
    context_object_name = "ds_staff_group"
    
    # queryset data
    def get_queryset(self):
        #Menu Model Class return use By slug
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.name_of_slug))
        queryset = Staff_Group.objects.filter(is_active=True).order_by('-lvl')#user__is_active=True,user__is_staff=True
        return queryset

    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": self.menu.title ,
            "title": self.menu.title,
            "keywords": self.menu.title,
            "author": development.BLOG_AUTHOR,
            "page_title":self.menu.title,
        })
        return context
#===============>

from django.shortcuts import render
from django.views.generic import TemplateView
from pytube.settings import base,development

# Create your views here.
class IndexView(TemplateView):
    template_name = "home/index.html"
    
     #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Home',
            "title": 'Home',
            "keywords": 'Home',
            "author": development.BLOG_AUTHOR,
            "page_title":'Welcome to Pytube, <br><em> the Most Exciting website of world! </em>',
        })
        return context
    
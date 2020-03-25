import datetime
import os
from django import template
from page.models import Menu

#call register library
register = template.Library()

nav_template_url="includes/nav_menu.html"

@register.inclusion_tag(nav_template_url, takes_context=True)
def load_menu(context,css_class):
    context['menu'] = Menu.objects.filter(parent=None, status=True).order_by("tree_id")
    #pass Custom css Class
    context['css_class'] =css_class
    return context

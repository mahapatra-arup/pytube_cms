import datetime
import os
from django import template
from page.models import Menu

#call register library
register = template.Library()

@register.inclusion_tag('includes/nav_menu.html', takes_context=True)
def load_menu(context,css_class):
    context['menu'] = Menu.objects.filter(parent=None, status=True).order_by("lvl")
    #pass Custom css Class
    context['css_class'] =css_class
    return context

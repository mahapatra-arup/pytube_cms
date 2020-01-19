import datetime
import os
from django import template
from post.models import Post
from pytube.constant_fields import *

#call register library
register = template.Library()

#Template
slider_template_url="includes/slider.html"
#Slider tag
@register.inclusion_tag(slider_template_url, takes_context=True)
def load_slider(context):
    context['home_slider'] = Post.objects.filter(term__name=CONST_SLIDER_TERM).order_by("updated_on")
    return context


#Template
notice_template_url="includes/notice_widget.html"
#Notice tag
@register.inclusion_tag(notice_template_url, takes_context=True)
def load_notice(context):
    context['home_notice'] = Post.objects.filter(term__name=CONST_NOTICE_TERM).order_by("updated_on")
    return context



#Template
event_template_url="includes/event_widget.html"
#Notice tag
@register.inclusion_tag(event_template_url, takes_context=True)
def load_event(context):
    context['home_event'] = Post.objects.filter(term__name=CONST_EVENT_TERM).order_by("updated_on")
    return context

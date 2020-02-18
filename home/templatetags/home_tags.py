import datetime
import os
from django import template
from post.models import Post
from organization.models import Org_Details
from pytube.constant_fields import *

#call register library
register = template.Library()

#Template
slider_template_url="includes/slider.html"
#Slider tag
@register.inclusion_tag(slider_template_url, takes_context=True)
def load_slider(context):
    context['home_slider'] = Post.objects.filter(term__name=WIDGET_SLIDER_TERM).order_by("updated_on")
    return context


#Template
notice_template_url="includes/notice_widget.html"
#notice tag
@register.inclusion_tag(notice_template_url, takes_context=True)
def load_notice(context):
    context['widget_notice'] = Post.objects.filter(term__name=WIDGET_NOTICE_TERM).order_by("updated_on")
    return context



#Template
event_template_url="includes/event_widget.html"
#event widget
@register.inclusion_tag(event_template_url, takes_context=True)
def load_event(context):
    context['widget_event'] = Post.objects.filter(term__name=WIDGET_EVENT_TERM).order_by("updated_on")
    return context


#Template
document_template_url="includes/document_widget.html"
#document widget
@register.inclusion_tag(document_template_url, takes_context=True)
def load_document(context):
    context['widget_document'] = Post.objects.filter(term__name=WIDGET_DOCUMENT_TERM).order_by("updated_on")
    return context


#Template
site_footer_template_url="includes/site_footer.html"
#site footer
@register.inclusion_tag(site_footer_template_url, takes_context=True)
def load_site_footer(context):
    context['orgdetails'] = Org_Details.objects.all().first()
    return context

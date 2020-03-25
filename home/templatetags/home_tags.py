import datetime
import os
from django import template
from post.models import Post, Term
from organization.models import Org_Details
from staff.models import Staff
from pytube.constant_fields import *

#call register library
register = template.Library()

###---widgets------------------------------------------------------------------------>
#Template
slider_template_url="widget/slider.html"
#Slider tag
@register.inclusion_tag(slider_template_url, takes_context=True)
def load_slider(context):
    context['home_slider'] = Post.objects.filter(status='Published', term__name=WIDGET_SLIDER_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_SLIDER_TERM).first(),
        })

    return context


#Template
service_template_url="widget/service_widget.html"
#Service widget
@register.inclusion_tag(service_template_url, takes_context=True)
def load_service(context):
    context['widget_service'] = Post.objects.filter(status='Published', term__name=WIDGET_SERVICE_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_SERVICE_TERM).first(),
        })
    return context

#Template
client_template_url="widget/client_widget.html"
#Service widget
@register.inclusion_tag(client_template_url, takes_context=True)
def load_client(context):
    context['widget_client'] = Post.objects.filter(status='Published', term__name=WIDGET_CLIENT_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_CLIENT_TERM).first(),
        })
    return context


#Template
testimonial_template_url="widget/testimonial_widget.html"
#Service widget
@register.inclusion_tag(testimonial_template_url, takes_context=True)
def load_testimonial(context):
    context['widget_testimonial'] = Staff.objects.filter(user__is_active=True,user__is_staff=True).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_TESTIMONIAL_TERM).first(),
        })
    return context

#--------------------------------------------------------------------------------------------------------------------->
#Template
notice_template_url="widget/notice_widget.html"
#notice tag
@register.inclusion_tag(notice_template_url, takes_context=True)
def load_notice(context):
    context['widget_notice'] = Post.objects.filter(status='Published', term__name=WIDGET_NOTICE_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_NOTICE_TERM).first(),
        })
    return context



#Template
event_template_url="widget/event_widget.html"
#event widget
@register.inclusion_tag(event_template_url, takes_context=True)
def load_event(context):
    context['widget_event'] = Post.objects.filter(status='Published', term__name=WIDGET_EVENT_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_EVENT_TERM).first(),
        })
    return context

#Template
post_template_url="widget/post_widget.html"
#post widget
@register.inclusion_tag(post_template_url, takes_context=True)
def load_post(context):
    context['widget_post'] = Post.objects.filter(status='Published', term__name=WIDGET_POST_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_POST_TERM).first(),
        })
    return context


#Template
document_template_url="widget/document_widget.html"
#document widget
@register.inclusion_tag(document_template_url, takes_context=True)
def load_document(context):
    context['widget_document'] = Post.objects.filter(status='Published', term__name=WIDGET_DOCUMENT_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_DOCUMENT_TERM).first(),
        })
    return context



#Template
weather_template_url="widget/weather_widget.html"
#document widget
@register.inclusion_tag(weather_template_url, takes_context=True)
def load_weather(context):
    context['widget_weather'] = Post.objects.filter(status='Published', term__name=WIDGET_WEATHER_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_WEATHER_TERM).first(),
        })
    return context



#Template
content_template_url="widget/content_widget.html"
#document widget
@register.inclusion_tag(content_template_url, takes_context=True)
def load_content(context):
    context['widget_content'] = Post.objects.filter(status='Published', term__name=WIDGET_CONTENT_TERM).order_by("updated_on")
    context.update({
            "term_data": Term.objects.filter(name=WIDGET_CONTENT_TERM).first(),
        })
    return context



### Inclues------------------------------------------------------------------>
#Template
site_footer_template_url="includes/site_footer.html"
#site footer
@register.inclusion_tag(site_footer_template_url, takes_context=True)
def load_site_footer(context):
    context['orgdetails'] = Org_Details.objects.all().first()
    return context


#load Org_Details
@register.simple_tag
def get_org_details():
    return Org_Details.objects.all().first()
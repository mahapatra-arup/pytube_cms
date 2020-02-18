import os
from django import template
import sys
from pytube.settings.development import PROJECT_ROOT_PATH  
from pytube.utils.ptutils import convert_to_size

register = template.Library()

@register.filter
def filesize(value):
    """Returns the filesize of the filename given in value"""
    root = PROJECT_ROOT_PATH
    # print (PROJECT_ROOT_PATH)
    return convert_to_size(os.path.getsize(root+value))

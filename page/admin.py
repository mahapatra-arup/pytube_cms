from django.contrib import admin
from .models import Menu,Page_Template,Contact_Us

#
# encoding: utf-8

from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin

class MenuAdmin(DraggableMPTTAdmin):
     # specify pixel amount for this ModelAdmin only:
    mptt_level_indent =20
    mptt_indent_field = "title"

    list_display = ('tree_actions','indented_title',#must use  fot mptt
    'title', 'has_children','page_template','icon_class','url', 'status', #modelo field
    'tree_id','level','lft','rght',) #mptt  field on datbase

    list_display_links=('indented_title',)#must use  fot mptt

admin.site.register(Menu, MenuAdmin)

@admin.register(Page_Template)
class Page_TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active', 'description',)    


@admin.register(Contact_Us)
class Contact_UsAdmin(admin.ModelAdmin):
    list_per_page = 7
    list_display = ('user','is_read','name', 'email', 'subject', 'content','created_on',)
    list_filter = ['user','name', 'email', 'subject', 'content','is_read',]
    list_display_links=('user','name', 'email', 'subject', 'content',)
    #list_editable = ['is_read',]

    readonly_fields = ('user','name', 'email', 'subject', 'content',)#Read Only
  
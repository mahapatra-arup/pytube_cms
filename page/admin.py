from django.contrib import admin
from .models import Menu,Page_Template

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'lvl', 'status','has_children','template_name',)
   
    #menu template get
    def template_name(self,obj):
        return obj.page_template.name

@admin.register(Page_Template)
class Page_TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_active', 'description',)    
  
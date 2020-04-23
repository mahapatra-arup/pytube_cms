from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tags,Term,Gal_Image,Comments
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import csv


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

#model admin=====
@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'slug', 'description', 'position','is_active',)
    list_filter = ['name', 'slug', 'description', 'position','is_active',]

    list_editable = ['description', 'position','is_active',]

    # readonly_fields = ('name',)#Read Only

    #remove edit delete button
    # def has_add_permission(self, request):
    #    return False
    # def has_change_permission(self, request, obj=None):
    #     return False
    def has_delete_permission(self, request, obj=None):
        return False

   


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['description','is_active',]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Gal_Image)
class Gal_ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photo_view')
    fields = ('name','photo','get_photo_view')     
    readonly_fields = ('get_photo_view',)
    
    def get_photo_view(self,obj):
        if obj.photo:
            return mark_safe('<a href="{url}"><img src="{url}" width="50px" height="50px" /></a>'.format(
                url=obj.photo.url))
        else:
            return mark_safe('')
        
     
# Post---------------------------------------->
@admin.register(Post)
class PostAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ('title','menu_name', 'user', 'term','category',  'status','featured_image_view','photos_count','slug')
    list_filter =('title','menu','term', 'user', 'category', 'status', 'slug')
    
    filter_horizontal = ("tags",)
    readonly_fields = ["featured_image_view",]
    actions = ["export_as_csv"]


    # prepopulated_fields = {'slug': ('title','category',)}
    list_editable = ['category','status',]
    list_per_page = 10
    
    list_select_related = ('menu',)
    #
    empty_value_display = '---'

    #image show
    def featured_image_view(self, obj):
        if obj.featured_image:
           return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url = obj.featured_image.url,
            width= 30,   #obj.featured_image.width,
            height=30,   #obj.featured_image.height,
            ) )
        else:
            return mark_safe('')

   #photos Count
    def photos_count(self,obj):
        return obj.photos.all().count()

    #menu name view
    def menu_name(self,obj):
        return obj.menu.title

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user','approved', 'content','post','updated_on','has_children','parent',)
    list_editable = ['approved',]
    pass


#Notice--------------------------------------->
# class  NoticeProxy(Post):
#     class Meta:
#         proxy = True

# @admin.register(NoticeProxy)
# class NoticeAdmin(admin.ModelAdmin):
#     list_display = ('title',  'user', 'category', 'status','get_image_url')
  
#     filter_horizontal = ("tags",)
    
    #only select Notice
    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #    if db_field.name == "term":
    #        kwargs["queryset"] = Term.objects.filter(name__in=['Notices',])
    #    return super().formfield_for_foreignkey(db_field, request, **kwargs)







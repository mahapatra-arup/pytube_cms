from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tags,Term


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'is_active')



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'category', 'status','get_image_url')
    filter_horizontal = ("tags",)
     #Tinmce======
    #class Media:
        #css = {
            # "screen": ("css/items/items.css",)
        # }
       # js = ("tinymce/tinymce.min.js",
       # "tinymce/init-tinymce.js",
       #S )

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')







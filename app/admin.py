from django.contrib import admin
from .models import Document_File

# Register your models here.
@admin.register(Document_File)
class Document_FileAdmin(admin.ModelAdmin):
    list_display = ('upload', 'is_image')

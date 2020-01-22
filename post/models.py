from django.db import models
from django.conf import settings
from django.utils.text import slugify
import datetime
import os
import uuid
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from tinymce import HTMLField
from page.models  import Menu

# Create your models here.



ROLE_CHOICE = (
    ('Admin', 'Admin'),
    ('Publisher', 'Publisher'),
    ('Author', 'Author'),
)

STATUS_CHOICE = (
    ('Drafted', 'Drafted'),
    ('Published', 'Published'),
    ('Rejected', 'Rejected'),
    ('Trashed', 'Trashed'),
)

#Term----------------------->
class Term (models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Term'
        verbose_name_plural = 'Term'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Term, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def Term_posts(self):
        return Post.objects.filter(category=self).count()

#Category------------------->
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    meta_keywords = models.TextField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = "pt_Category"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def category_posts(self):
        return Post.objects.filter(category=self).count()

#Tag------------------------>
class Tags(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "pt_Tags"

    def save(self, *args, **kwargs):
        tempslug = slugify(self.name)
        if self.id:
            tag = Tags.objects.get(pk=self.id)
            if tag.name != self.name:
                self.slug =self.create_tag_slug(tempslug)
        else:
            self.slug = self.create_tag_slug(tempslug)
        super(Tags, self).save(*args, **kwargs)

       

    def __str__(self):
        return self.name

    def create_tag_slug(self,tempslug):
        slugcount = 0
        while True:
            try:
                Tags.objects.get(slug=tempslug)
                slugcount += 1
                tempslug = tempslug + '-' + str(slugcount)
            except ObjectDoesNotExist:
                return tempslug
from django.utils.safestring import mark_safe


#Gallery Images
class Gal_Image(models.Model):
    name = models.CharField(max_length=100, null=False)
    photo = models.ImageField(upload_to='post/Gal_Image/%Y/%m/%d',null=True, blank=True)

    class Meta:
        db_table = "gal_image"
        verbose_name = 'Gallery Images'
        verbose_name_plural = 'Gallery Images'

    @property
    def get_image_url(self):
         if self.photo and hasattr(self.photo, 'url'):
          return self.photo.url

    def __str__(self):
         return self.name
         
#Post----------------------->
class Post(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,help_text="say's that the data will be insert in which Web page");
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content = HTMLField("content")
    term=models.ForeignKey(Term,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name='rel_posts')

    meta_description = models.TextField(max_length=160, null=True, blank=True)
    keywords = models.TextField(max_length=500, blank=True)

    featured_image = models.ImageField(upload_to='post/images/%Y/%m/%d/', blank=True, null=True,help_text='Maximum file size allowed is 200kb')
    document_file = models.FileField(upload_to='post/documents/%Y/%m/%d/', blank=True, null=True)
    
    #For gallery
    photos = models.ManyToManyField(Gal_Image, blank=True,related_name='rel_post_galimg')

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Published')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated_on']

   
    def save(self, *args, **kwargs):
        tempslug = slugify(self.title)
        if self.id:
            blogpost = Post.objects.get(pk=self.id)
            if blogpost.title != self.title:
                self.slug = create_slug(tempslug)
        else:
            self.slug = create_slug(tempslug)
            #self.email_to_admins_on_post_create()

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    ###get_image_url
    @property
    def get_image_url(self):
         if self.featured_image and hasattr(self.featured_image, 'url'):
          return self.featured_image.url
    @property
    def get_document_url(self):
         if self.document_file and hasattr(self.document_file, 'url'):
          return self.document_file.url  
   
   

        


def create_slug(tempslug):
    slugcount = 0
    while True:
        try:
            Post.objects.get(slug=tempslug)
            slugcount += 1
            tempslug = tempslug + '-' + str(slugcount)
        except ObjectDoesNotExist:
            return tempslug


  



     
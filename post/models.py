from django.db import models
from django.conf import settings
from django.utils.text import slugify
import datetime
import os
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from tinymce import HTMLField
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




#Post----------------------->
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content = HTMLField("content")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name='rel_posts')
    term=models.ForeignKey(Term,on_delete=models.CASCADE)

    meta_description = models.TextField(max_length=160, null=True, blank=True)
    
    keywords = models.TextField(max_length=500, blank=True)
    featured_image = models.ImageField(upload_to='post/uploads/%Y/%m/%d/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Published')
   
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

    ###
    @property
    def get_image_url(self):
         if self.featured_image and hasattr(self.featured_image, 'url'):
          return self.featured_image.url

def create_slug(tempslug):
    slugcount = 0
    while True:
        try:
            Post.objects.get(slug=tempslug)
            slugcount += 1
            tempslug = tempslug + '-' + str(slugcount)
        except ObjectDoesNotExist:
            return tempslug


  



     
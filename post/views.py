from django.shortcuts import get_list_or_404, get_object_or_404, render
from post.models import Post,Category,Tags
from django.views.generic import ListView, DetailView
from django.db.models import Count
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
#settings
from pytube.settings import base,development
from pytube.constant_fields import *
from page.models import Menu  # menu Import

#menuwise data
def categories_tags_lists(menu_title):
    #categories
    categories_list = Category.objects.filter(is_active=True, post__status='Published', post__menu__title=menu_title).distinct()
  
   #tags
    tags_list = Tags.objects.annotate(
        Num=Count('rel_posts')).filter(Num__gt=0, rel_posts__status='Published', rel_posts__category__is_active=True)[:20]
    

    return {'categories_list': categories_list, 'tags_list': tags_list}


#<===================
#Post View==
class PostListView(ListView):
    #Custom var
    name_of_slug="menu_slug"

     #fixed
    template_name = "post/post_list.html"
    context_object_name = "ds_posts"
    
    # queryset data
    def get_queryset(self):
        #Menu Model Class return use By slug
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.name_of_slug))
        queryset = Post.objects.filter(menu=self.menu,category__is_active=True,status='Published').order_by('-updated_on')
        return queryset
    
    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(self.menu.slug)
        #Menu Data Pass
        #perameter(must be)
        context.update({
            "menu_name_slug": self.menu.slug,
        })

        #page data(optional)
        context.update({
            "description": self.menu.title ,
            "title": self.menu.title,
            "keywords": self.menu.title,
            "author": development.BLOG_AUTHOR,
            "page_title":self.menu.title,
        })
      
       #menu wise side data like Category/archive
        context.update(categories_tags_lists(self.menu.title))

        return context

class PostDetailView(DetailView):
    #Custom var
    name_of_slug="post_slug"

    #system var Fixed
    template_name = 'post/post_detail.html'
    model = Post
    slug_url_kwarg = name_of_slug 
    context_object_name = "ds_posts_detail"
     #end

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context.update({
            "description": 'Post Details',
            "title": 'Post Details',
            "keywords": 'Post Details',
            "author": development.BLOG_AUTHOR,
            "page_title":'Post Details',
        })
        return context
#===============>

#<===================
#Notice View==
class NoticeListView(ListView):
    #custom
    term_value=CONST_NOTICE_TERM 

     #fixed
    template_name = "notice/notice_list.html"
    queryset = Post.objects.filter(status='Published', category__is_active=True, term__name=term_value).order_by('-updated_on')
    context_object_name = "ds_posts"

    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Notice',
            "title": 'Notice',
            "keywords": 'Notice',
            "author": development.BLOG_AUTHOR,
            "page_title":'Notice',
        })
        
        return context
#===============>


#<===================
#Gallery list View==
class GalleryListView(ListView):
    #custom
    term_value=CONST_GALLERY_TERM

     #fixed
    template_name = "gallery/gallery_list.html"
    queryset = Post.objects.filter(status='Published', category__is_active=True, term__name=term_value).order_by('-updated_on')
    context_object_name = "ds_posts"

    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'Galleries',
            "title": 'Galleries',
            "keywords": 'Galleries',
            "author": development.BLOG_AUTHOR,

            "page_title":'Galleries',
        })
        context.update(categories_tags_lists(self.term_value))
        return context

class GalleryDetailView(DetailView):
    #Custom var
    name_of_slug="gallery_slug"
    # name_of_urlspath="gallery_detail"#this is available on urls.py -->path--->name
    # term_value=CONST_GALLERY_TERM 

    #system var Fixed
    template_name = 'gallery/gallery_detail.html'
    model = Post
    slug_url_kwarg = name_of_slug 
    context_object_name = "ds_posts_detail"
     #end

    def get_context_data(self, *args, **kwargs):
        context = super(GalleryDetailView, self).get_context_data(*args, **kwargs)
        context.update({
            "description": 'Gallery Details',
            "title": 'Gallery Details',
            "keywords": 'Gallery Details',
            "author": development.BLOG_AUTHOR,
            "page_title":'Gallery Details',
        })
        return context
#===============>

class SelectedCategoryView(ListView):
    #Custom var
    category_slug="category_slug"
    menu_slug="menu_slug"

     #fixed
    template_name = "post/post_list.html"
    context_object_name = "ds_posts"
    
    # queryset data
    def get_queryset(self):
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.menu_slug)) #\\
        self.category = get_object_or_404(Category, slug=self.kwargs.get(self.category_slug))
        queryset = Post.objects.filter(category=self.category,menu=self.menu,category__is_active=True,status='Published').order_by('-updated_on')
        return queryset

    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #Menu Data Pass
        #perameter(must be)
        context.update({
            "menu_name_slug": self.menu.slug,
        })

        # //page data 
        user = self.category.user
        author = user.first_name if user.first_name else user.username

        context.update({
            "description": self.category.description,
            "title": self.category.name,
            "keywords": self.category.meta_keywords,
            "author": author,
            "page_title":self.category.name+' / '+self.menu.title  ,
        })
       
       #Term wise side data like Category/archive
        context.update(categories_tags_lists(self.menu.title))
        return context

class SelectedTagView(ListView):
    template_name = "posts/new_index.html"
    context_object_name = "blog_posts"

    def get_queryset(self):
        self.tag = get_object_or_404(Tags, slug=self.kwargs.get("tag_slug"))
        return get_list_or_404(Post, tags=self.tag, status='Published', category__is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(SelectedTagView, self).get_context_data(*args, **kwargs)
        context.update({
            "description": self.tag.name,
            "title": self.tag.name,
            "keywords": self.tag.name,
            "author": development.BLOG_AUTHOR,
            "tag": self.tag,
        })
        context.update(categories_tags_lists())
        return context

class ArchiveView(ListView):
    template_name = "posts/new_index.html"
    context_object_name = "blog_posts"

    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        self.date = datetime(int(year), int(month), 1)
        
        return Post.objects.filter(
            category__is_active=True, status="Published", updated_on__year=year, updated_on__month=month).order_by('-updated_on')

    def get_context_data(self, *args, **kwargs):
        context = super(ArchiveView, self).get_context_data(*args, **kwargs)
        context.update({
            "description": "Blog Archive - " + self.date.strftime("%B %Y"),
            "title": "Blog Archive - " + self.date.strftime("%B %Y"),
            "keywords": "Blog Archive - " + self.date.strftime("%B %Y"),
            "author": development.BLOG_AUTHOR,
            "date": self.date,
        })
        context.update(categories_tags_lists())
        return context


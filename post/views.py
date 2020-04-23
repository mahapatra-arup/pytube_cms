
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from post.models import Category, Comments, Post, Tags
from django.views.generic import ListView, DetailView
from django.db.models import Count
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

#decorator for login required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#settings
from pytube.settings import base,development
from pytube.constant_fields import *

from page.models import Menu  # menu Import

#Form
from .forms import CommentForm
from django.contrib import messages

#menuwise data
def categories_tags_lists(menu_title):
    #categories
    categories_list = Category.objects.filter(is_active=True, post__status='Published', post__menu__title=menu_title).distinct()
  
   #tags (rel_posts = use in model related_name)
    tags_list = Tags.objects.annotate(
        Num=Count('rel_posts')).filter(Num__gt=0, rel_posts__status='Published',rel_posts__menu__title=menu_title, rel_posts__category__is_active=True)[:20]
    

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
        # print(self.menu.slug)
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
            "breadcrumb":self.menu.title,
        })
      
       #menu wise side data like Category/archive
        context.update(categories_tags_lists(self.menu.title))

        return context

class PostDetailView(DetailView):
    #Custom var
    name_of_slug="post_slug"
    form=CommentForm()
    success_url = "post_detail"#name of Post Details URL

    #system var Fixed
    template_name = 'post/post_detail.html'
    model = Post
    slug_url_kwarg = name_of_slug 
    context_object_name = "ds_posts_detail"
     #end

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #print(self.get_object().title)

        # //Auther
        user = self.get_object().user
        author = user.first_name if user.first_name else user.username
        menu_detail=self.get_object().menu

        context.update({
            "description": self.get_object().meta_description,
            "title": self.get_object().title,
            "keywords": self.get_object().keywords,
            "author": author,
            "page_title":self.get_object().title,
            "breadcrumb":menu_detail.title+' / '+self.get_object().title,
        }) 
        
        #Comment form
        context['form'] = self.form   
        return context

    #comment save
    @method_decorator(login_required) 
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        #For Child
        self.parent_id = self.request.POST.get('parent_id')
        
        if form.is_valid():
            post = self.get_object()
            comment = form.save(commit=False)
            comment.post= post
            comment.user = request.user
            if self.parent_id:
               comment.parent_id=int(self.parent_id) #'parent_id' db Field Name
            
            comment.save()

            messages.add_message(request, messages.INFO ,'Comment Post Successfull : waiting for approval',extra_tags='Comment', fail_silently=True)
            return HttpResponseRedirect(reverse_lazy(self.success_url,args=
            [post.slug]))

#===============>

#<===================
#Notice View=
class NoticeListView(ListView):
    #Custom var
    name_of_slug="menu_slug"

     #fixed
    template_name = "notice/notice_list.html"
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
       
        #Menu Data Pass
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
            "breadcrumb":self.menu.title,
        })
      
       #menu wise side data like Category/archive
        context.update(categories_tags_lists(self.menu.title))

        return context
#===============>


#<===================
#Gallery list View==
class GalleryListView(ListView):
    #Custom var
    name_of_slug="menu_slug"

     #fixed
    template_name = "gallery/gallery_list.html"
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
            "breadcrumb":self.menu.title,
        })
      
       #menu wise side data like Category/archive
        context.update(categories_tags_lists(self.menu.title))

        return context

class GalleryDetailView(DetailView):
    #Custom var
    name_of_slug="gallery_slug"

    #system var Fixed
    template_name = 'gallery/gallery_detail.html'
    model = Post
    slug_url_kwarg = name_of_slug 
    context_object_name = "ds_posts_detail"
     #end

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #print(self.get_object().title)

        # //Auther
        user = self.get_object().user
        author = user.first_name if user.first_name else user.username
        menu_detail=self.get_object().menu

        context.update({
            "description": self.get_object().meta_description,
            "title": self.get_object().title,
            "keywords": self.get_object().keywords,
            "author": author,
            "page_title":self.get_object().title,
            "breadcrumb":menu_detail.title+' / '+self.get_object().title,
        })
        return context
#===============>


#--Post------------------------------------------------------------>
class SelectedCategoryView(ListView):
    #Custom var
    category_slug="category_slug"
    menu_slug="menu_slug"
   

     #fixed
    context_object_name = "ds_posts"
    template_name = "post/post_list.html"
    
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
            "page_title":self.menu.title,
            "breadcrumb": self.menu.title +' / '+self.category.name,
        })
       
       #Term wise side data like Category/archive
        context.update(categories_tags_lists(self.menu.title))
        return context

class ArchiveView(ListView):
    #Custom var
    menu_slug="menu_slug"

     #fixed
    template_name = "post/post_list.html"
    context_object_name = "ds_posts"

    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
       
        self.date = datetime.datetime.strptime('01/'+str(month)+'/'+str(year),'%d/%m/%Y')
        print(self.date)
        #
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.menu_slug)) #\\
        queryset = Post.objects.filter(menu=self.menu,category__is_active=True,status='Published',
            updated_on__year=year, updated_on__month=month,).order_by('-updated_on')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #Menu Data Pass
        context.update({
            "menu_name_slug": self.menu.slug,
        })

        # //page data 
        context.update({
            "author": self.menu.title,
            "page_title":self.menu.title,
            "description": "Blog Archive - " + self.date.strftime("%B %Y"),
            "title": "Blog Archive - " + self.date.strftime("%B %Y"),
            "keywords": "Blog Archive - " + self.date.strftime("%B %Y"),
            "breadcrumb": self.menu.title +' / '+ self.date.strftime("%B %Y"),

            "date": self.date,
        })   
        context.update(categories_tags_lists(self.menu.title))
        return context

class SelectedTagView(ListView):
     #Custom var
    menu_slug="menu_slug"
    tag_slug="tag_slug"

     #fixed
    template_name = "post/post_list.html"
    context_object_name = "ds_posts"

    def get_queryset(self):
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.menu_slug)) 
        self.tag = get_object_or_404(Tags, slug=self.kwargs.get(self.tag_slug))
       
        queryset = get_list_or_404(Post, tags=self.tag, menu=self.menu,category__is_active=True,status='Published')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #Menu Data Pass
        context.update({
            "menu_name_slug": self.menu.slug,
        })

        # //page data 
        context.update({
            "author": development.BLOG_AUTHOR,
            "page_title" : self.menu.title,
            "description": 'Tags - '+self.tag.name,
            "title": 'Tags - '+self.tag.name,
            "keywords": 'Tags - '+self.tag.name,
            "breadcrumb": self.menu.title +' / '+ self.tag.name,

            "tag": self.tag,
        })   
        context.update(categories_tags_lists(self.menu.title))
        return context    


#---Gallery-------------------------------------------------------->
class SelectedGalCategoryView(ListView):
    #Custom var
    category_slug="category_slug"
    menu_slug="menu_slug"
   

     #fixed
    context_object_name = "ds_posts"
    template_name = "gallery/gallery_list.html"
    
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
            "page_title":self.menu.title,
            "breadcrumb": self.menu.title +' / '+self.category.name,
        })
       
       #Term wise side data like Category/archive
        context.update(categories_tags_lists(self.menu.title))
        return context

class GalArchiveView(ListView):
    #Custom var
    menu_slug="menu_slug"

     #fixed
    template_name = "gallery/gallery_list.html"
    context_object_name = "ds_posts"

    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
       
        self.date = datetime.datetime.strptime('01/'+str(month)+'/'+str(year),'%d/%m/%Y')
        print(self.date)
        #
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.menu_slug)) #\\
        queryset = Post.objects.filter(menu=self.menu,category__is_active=True,status='Published',
            updated_on__year=year, updated_on__month=month,).order_by('-updated_on')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #Menu Data Pass
        context.update({
            "menu_name_slug": self.menu.slug,
        })

        # //page data 
        context.update({
            "author": self.menu.title,
            "page_title":self.menu.title,
            "description": "Blog Archive - " + self.date.strftime("%B %Y"),
            "title": "Blog Archive - " + self.date.strftime("%B %Y"),
            "keywords": "Blog Archive - " + self.date.strftime("%B %Y"),
            "breadcrumb": self.menu.title +' / '+ self.date.strftime("%B %Y"),

            "date": self.date,
        })   
        context.update(categories_tags_lists(self.menu.title))
        return context

class SelectedGalTagView(ListView):
     #Custom var
    menu_slug="menu_slug"
    tag_slug="tag_slug"

     #fixed
    template_name = "gallery/gallery_list.html"
    context_object_name = "ds_posts"

    def get_queryset(self):
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.menu_slug)) 
        self.tag = get_object_or_404(Tags, slug=self.kwargs.get(self.tag_slug))
       
        queryset = get_list_or_404(Post, tags=self.tag, menu=self.menu,category__is_active=True,status='Published')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #Menu Data Pass
        context.update({
            "menu_name_slug": self.menu.slug,
        })

        # //page data 
        context.update({
            "author": development.BLOG_AUTHOR,
            "page_title" : self.menu.title,
            "description": 'Tags - '+self.tag.name,
            "title": 'Tags - '+self.tag.name,
            "keywords": 'Tags - '+self.tag.name,
            "breadcrumb": self.menu.title +' / '+ self.tag.name,

            "tag": self.tag,
        })   
        context.update(categories_tags_lists(self.menu.title))
        return context    


#Notice------------------------------------------------------------>
class SelectedNoticeCategoryView(ListView):
    #Custom var
    category_slug="category_slug"
    menu_slug="menu_slug"
   

     #fixed
    context_object_name = "ds_posts"
    template_name = "notice/notice_list.html"
    
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
            "page_title":self.menu.title,
            "breadcrumb": self.menu.title +' / '+self.category.name,
        })
       
       #Term wise side data like Category/archive
        context.update(categories_tags_lists(self.menu.title))
        return context

class NoticeArchiveView(ListView):
    #Custom var
    menu_slug="menu_slug"

     #fixed
    template_name = "notice/notice_list.html"
    context_object_name = "ds_posts"

    def get_queryset(self):
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
       
        self.date = datetime.datetime.strptime('01/'+str(month)+'/'+str(year),'%d/%m/%Y')
        print(self.date)
        #
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.menu_slug)) #\\
        queryset = Post.objects.filter(menu=self.menu,category__is_active=True,status='Published',
            updated_on__year=year, updated_on__month=month,).order_by('-updated_on')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        #Menu Data Pass
        context.update({
            "menu_name_slug": self.menu.slug,
        })

        # //page data 
        context.update({
            "author": self.menu.title,
            "page_title":self.menu.title,
            "description":  self.date.strftime("%B %Y"),
            "title":  self.date.strftime("%B %Y"),
            "keywords":  self.date.strftime("%B %Y"),
            "breadcrumb": self.menu.title +' / '+ self.date.strftime("%B %Y"),

            "date": self.date,
        })   
        context.update(categories_tags_lists(self.menu.title))
        return context

class SelectedNoticeTagView(ListView):
     #Custom var
    menu_slug="menu_slug"
    tag_slug="tag_slug"

     #fixed
    template_name = "notice/notice_list.html"
    context_object_name = "ds_posts"

    def get_queryset(self):
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.menu_slug)) 
        self.tag = get_object_or_404(Tags, slug=self.kwargs.get(self.tag_slug))
       
        queryset = get_list_or_404(Post, tags=self.tag, menu=self.menu,category__is_active=True,status='Published')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        #Menu Data Pass
        context.update({
            "menu_name_slug": self.menu.slug,
        })

        # //page data 
        context.update({
            "author": development.BLOG_AUTHOR,
            "page_title" : self.menu.title,
            "description": 'Tags - '+self.tag.name,
            "title": 'Tags - '+self.tag.name,
            "keywords": 'Tags - '+self.tag.name,
            "breadcrumb": self.menu.title +' / '+ self.tag.name,

            "tag": self.tag,
        })   
        context.update(categories_tags_lists(self.menu.title))
        return context    

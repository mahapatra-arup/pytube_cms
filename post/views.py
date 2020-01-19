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

#term means Post/notice/gallery/etc identifire
def categories_tags_lists(term_value):
    #categories
    categories_list = Category.objects.filter(is_active=True, post__status='Published', post__term__name=term_value).distinct()
  
   #tags
    tags_list = Tags.objects.annotate(
        Num=Count('rel_posts')).filter(Num__gt=0, rel_posts__status='Published', rel_posts__category__is_active=True)[:20]
    
    #Recent posts
    posts = Post.objects.filter(status='Published').order_by('-updated_on')[0:3]

    return {'categories_list': categories_list, 'tags_list': tags_list, 'recent_posts': posts}


#<===================
#Post View==
class PostListView(ListView):
    #custom
    term_value=CONST_POST_TERM 

     #fixed
    template_name = "post/post_list.html"
    queryset = Post.objects.filter(status='Published', category__is_active=True, term__name=term_value).order_by('-updated_on')
    context_object_name = "ds_posts"

    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'post',
            "title": 'Post',
            "keywords": 'post',
            "author": development.BLOG_AUTHOR,
            "page_title":'Post',
        })
        context.update(categories_tags_lists(self.term_value))
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
        context.update(categories_tags_lists(self.term_value))
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

class BlogPostView(DetailView):
    template_name = 'posts/new_blog_view.html'
    model = Post
    slug_url_kwarg = "blog_slug"
    context_object_name = "blog_name"


    term_value=CONST_GALLERY_TERM 
    def dispatch(self, request, *args, **kwargs):
        self.object = Post.objects.filter(slug=kwargs.get("blog_slug")).last()
        if not self.object:
            #
            post_slug = get_object_or_404(Post, slug=self.kwargs.get("blog_slug"))
            if self.kwargs.get("blog_slug") != post_slug.blog.slug:
                return HttpResponseRedirect(reverse('blog_post_view', kwargs={"blog_slug": post_slug.slug}), status=301)
        return super(BlogPostView, self).dispatch(request, *args, **kwargs)

    #def get_mini_url(self, request):
        #url = request.build_absolute_uri()
        #try:
            #api_key = os.getenv('API_KEY')
            #url = google_mini(url, api_key)
        #except Exception:
           #pass
        #return url

    def get_context_data(self, *args, **kwargs):
        context = super(BlogPostView, self).get_context_data(*args, **kwargs)
        user = self.object.user
        author = user.first_name if user.first_name else user.username
        related_posts = Post.objects.filter(
            status='Published',
            category=self.object.category,
            tags__in=self.object.tags.all()
        ).exclude(id=self.object.id).distinct()[:3]
        context.update({
            "related_posts": related_posts,
            #"disqus_shortname": getattr(settings, 'DISQUS_SHORTNAME'),
            "description": self.object.meta_description if self.object.meta_description else "",
            "title": self.object.title,
            "keywords": self.object.keywords,
            "author": author,
           # "short_url": self.get_mini_url(self.request),
            "blog_title": development.BLOG_AUTHOR
        })
        context.update(categories_tags_lists(term_value))
        return context

class SelectedCategoryView(ListView):
    template_name = "posts/new_index.html"
    context_object_name = "blog_posts"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get("category_slug"))
        return Post.objects.filter(category=self.category, category__is_active=True, status='Published')

    def get_context_data(self, *args, **kwargs):
        context = super(SelectedCategoryView, self).get_context_data(*args, **kwargs)
        user = self.category.user
        author = user.first_name if user.first_name else user.username
        context.update({
            "description": self.category.description,
            "title": self.category.name,
            "keywords": self.category.meta_keywords,
            "author": author,
            "category": self.category,
        })
        context.update(categories_tags_lists())
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


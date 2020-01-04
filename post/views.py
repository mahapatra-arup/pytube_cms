from django.shortcuts import render
from post.models import Post,Category,Tags
from django.views.generic import ListView, DetailView
from django.db.models import Count


def categories_tags_lists():
    categories_list = Category.objects.filter(is_active=True, post__status='Published').distinct()
    tags_list = Tags.objects.annotate(
        Num=Count('rel_posts')).filter(Num__gt=0, rel_posts__status='Published', rel_posts__category__is_active=True)[:20]
    posts = Post.objects.filter(status='Published').order_by('-updated_on')[0:3]
    return {'categories_list': categories_list, 'tags_list': tags_list, 'recent_posts': posts}

# Create your views here.
class PostListView(ListView):
     #
    template_name = "post/post_list.html"
    queryset = Post.objects.filter(status='Published', category__is_active=True).order_by('-updated_on')
    context_object_name = "ds_posts"

    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            "description": 'post',
            "title": 'Post',
            "keywords": 'post',
            "author": 'post',
        })
        #context.update(categories_tags_lists())
        return context
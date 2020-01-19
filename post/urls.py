"""pytube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from . import views
from post.views import *


urlpatterns = [
    #list View
     path('',PostListView.as_view(),name='post_list'),
     path('notice',NoticeListView.as_view(),name='notice_list'),
     path('gallery',GalleryListView.as_view(),name='gallery_list'),

    # Details View
     path('gallery/<slug:gallery_slug>/', GalleryDetailView.as_view(), name='gallery_detail'),#use in template

     #category/tags/archive
    path('category/<slug:category_slug>/', SelectedCategoryView.as_view(), name='selected_category'),
    path('tags/<slug:tag_slug>/', SelectedTagView.as_view(), name='selected_tag'),
    path('<year>/<month>/', ArchiveView.as_view(), name='archive_posts'),
    #path('<slug:blog_slug>/', BlogPostView.as_view(), name='blog_post_view'),
]

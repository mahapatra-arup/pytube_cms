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
    # menu_slug use iDentify menu data
     path('<slug:menu_slug>',PostListView.as_view(),name='post_list'),
     path('notice/<slug:menu_slug>/',NoticeListView.as_view(),name='notice_list'),
     path('gallery/<slug:menu_slug>/',GalleryListView.as_view(),name='gallery_list'),

    # Details View
     path('details/<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
     path('gallery/photos/<slug:gallery_slug>/', GalleryDetailView.as_view(), name='gallery_detail'),
     

     #category/tags/archive For POST
    path('category/<slug:menu_slug>/<category_slug>/', SelectedCategoryView.as_view(), name='selected_category'),
    path('archive/<slug:menu_slug>/<slug:year>/<slug:month>/', ArchiveView.as_view(), name='archive_posts'),
    path('tags/<slug:menu_slug>/<slug:tag_slug>/', SelectedTagView.as_view(), name='selected_tag'),

    #--#category/tags/archive For Gallery
    path('gallery/category/<slug:menu_slug>/<category_slug>/', SelectedGalCategoryView.as_view(), name='selected_Gallery_category'),
    path('gallery/archive/<slug:menu_slug>/<slug:year>/<slug:month>/', GalArchiveView.as_view(), name='Gallery_archive_posts'),
    path('gallery/tags/<slug:menu_slug>/<slug:tag_slug>/', SelectedGalTagView.as_view(), name='selected_Gallery_tag'),
    
    #--#category/tags/archive For Notice
    path('Notice/category/<slug:menu_slug>/<category_slug>/', SelectedNoticeCategoryView.as_view(), name='selected_Notice_category'),
    path('Notice/archive/<slug:menu_slug>/<slug:year>/<slug:month>/', NoticeArchiveView.as_view(), name='Notice_archive_posts'),
    path('Notice/tags/<slug:menu_slug>/<slug:tag_slug>/', SelectedNoticeTagView.as_view(), name='selected_Notice_tag'),
]

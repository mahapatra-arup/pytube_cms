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
from django.conf import settings
from django.conf.urls.static import static

#admin site config
admin.site.site_header = "Pytube Admin"
admin.site.site_title = "Pytube Admin Portal"
admin.site.index_title = "Welcome to Pytube CMS Portal"
#view site site url set
#admin.site.site_url = 'http://coffeehouse.com/'#ref:https://www.webforefront.com/django/admincustomlayout.html
#admin.empty_value_display = '**Empty**'


#Url-patterns Design
urlpatterns = [
    #admin App
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/pt/', admin.site.urls),

    path('newsletter/', include('newsletter.urls')),


    #Home Index App
    path('',include("home.urls")),
    #post App
    path('post/',include("post.urls")),
    #staff App
    path('staff/',include("staff.urls")),
    
     #page App
    path('page/',include("page.urls")),
    
    #3rd party App
    path('tinymce/', include('tinymce.urls')),

    #shop
    path('accounts/', include('allauth.urls')),
    path('shop/', include('shop.urls'))

]

#Media Root static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

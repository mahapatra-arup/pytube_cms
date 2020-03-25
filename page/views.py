from django.shortcuts import get_object_or_404, render
from django.views.generic import View,ListView,FormView
#Post
from post.models import Post
from django.db.models import Q
from pytube.settings import development
from page.models import Contact_Us, Menu

#forms 
from .forms import ContactUsForm


#Serach View------------------------------>
class SearchResultsView(ListView):
    model = Post
    template_name = 'page/search_results.html'
    

    def get_queryset(self): # new
        self.query = self.request.GET.get('s_str')#'s_str' -- This Is the 'Textbox' name

        if self.query is None:
            self.query=""
            
        object_list = Post.objects.filter(Q(title__icontains=self.query)|Q(content__icontains=self.query)|
               Q(meta_description__icontains=self.query) | Q(keywords__icontains=self.query)|
               Q(slug__icontains=self.query) | Q(created_on__icontains=self.query)|
               Q(updated_on__icontains=self.query) | 
            
               Q(term__name__icontains=self.query)|Q(user__username__icontains=self.query)|
               Q(category__name__icontains=self.query) | Q(tags__name__icontains=self.query)|
               Q(menu__title__icontains=self.query) |Q(photos__name__icontains=self.query)
            
        ).distinct()
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context.update({
            "serach_str":self.query ,
        })

        #page data(optional)
        context.update({
            "description": "Search Results" ,
            "title": "Search Results",
            "keywords": "Search Results, Post, Term, Category, Gallery, Page",
            "author": development.BLOG_AUTHOR,
            "page_title":"Search Results",
        })
      
        return context

# Create your views here.
class ContactUsView(FormView):
    form_class  = ContactUsForm
    template_name = 'page/contact_us.html'

    def get(self, request, *args, **kwargs):
        form  = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            #save
            self.save_data(form.cleaned_data)
            #mail send
            self.send_mail(form.cleaned_data)

            #new instance
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})

    def save_data(self, valid_data):
        contact=Contact_Us()
        contact.name=valid_data['name']
        contact.email=valid_data['email']
        contact.subject=valid_data['subject']
        contact.content=valid_data['content']
        contact.is_read=False
        contact.save()
        

    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data)
        pass


#Content Page------------------------------->
class ContentPageView(ListView):
    #Custom var
    name_of_slug="menu_slug"

     #fixed
    template_name = "page/content_page.html"
    context_object_name = "ds_posts"
    
    # queryset data
    def get_queryset(self):
        #Menu Model Class return use By slug
        self.menu = get_object_or_404(Menu, slug=self.kwargs.get(self.name_of_slug))
        queryset = Post.objects.filter(menu=self.menu,status='Published').order_by('-updated_on')
        return queryset
    
    #method
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # print(self.menu.slug)
        #Menu data
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
        return context

from django.shortcuts import render
from django.views.generic import View,ListView
#Post
from post.models import Post
from django.db.models import Q
from pytube.settings import development


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
class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact-us.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            self.send_mail(form.cleaned_data)
            form = ContactForm()
            return render(request, 'contact-us.html', {'form': form})
        return render(request, 'contact-us.html', {'form': form})

    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data)
        pass

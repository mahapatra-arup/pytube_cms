from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home/index.html",{
            'title':'Home',
            'page_title':'Welcome to Pytube, <br><em> the Most Exciting website of world! </em>'
        })
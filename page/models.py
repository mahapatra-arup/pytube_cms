from django.db import models


VIEW_TITLE_CHOICE = (
    ('Title', 'Title'),
    ('Image', 'Image'),
    ('Both', 'Both'),
)


#document Upload----------------------->
class Page_Template(models.Model):
    name = models.CharField(max_length=20, unique=True)
    url = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name    

class Menu(models.Model):
        parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)
        toolstrip=models.CharField(max_length=255)
        url = models.CharField(max_length=255, blank=True)
        status = models.BooleanField(default=True)
        lvl = models.IntegerField(blank=True)
        slug = models.SlugField()
        image=models.ImageField(upload_to='menu/', blank=True, null=True)
        view_title=models.CharField(max_length=10, choices=VIEW_TITLE_CHOICE, default='Both')


        def __str__(self):
            return self.title

        def get_children(self):
            return self.menu_set.all()

        def has_children(self):
            if self.get_children():
                return True
            return False

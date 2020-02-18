from django.db import models
from django.db.models import Max
from pytube.utils.ptutils import *

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

    class Meta:
            db_table = "Page_Template"
            verbose_name = 'Page Template'
            verbose_name_plural = 'Page Template'
    
    def __str__(self):
        return self.name    

class Menu(models.Model):
        parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
        page_template=models.ForeignKey(Page_Template,on_delete=models.CASCADE,help_text='Select Page Template');
        title = models.CharField(max_length=100)
        toolstrip=models.CharField(max_length=255,blank=True)
        url = models.CharField(max_length=255, blank=True,editable=False)
        status = models.BooleanField(default=True)
        lvl = models.IntegerField(blank=True)
        slug = models.SlugField(unique=True)
        image=models.ImageField(upload_to='menu/', blank=True, null=True)
        view_title=models.CharField(max_length=10, choices=VIEW_TITLE_CHOICE, default='Both')
        

        class Meta:
            db_table = "Menu"
            verbose_name = 'Menu'
            verbose_name_plural = 'Menu'


        def save(self, *args, **kwargs):
            
             #----------generate url field(copy url field from template)-----------
            if self.page_template:
                self.url=self.page_template.url
                
            #----------auto increment lavel-----------
            if self._state.adding: #only insert time work
                maxlvl= Menu.objects.all().aggregate(maxval=Max('lvl'))['maxval']  #field Name
                self.lvl= (int(maxlvl or 0)+1)

            #----------super Execute------------
            super(Menu, self).save(*args, **kwargs)

        def __str__(self):
            return self.title

        def get_children(self):
            return self.menu_set.all()

        def has_children(self):
            if self.get_children():
                return True
            return False

         

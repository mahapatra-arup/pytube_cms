from django.db import models
from django.db.models import Max
from pytube.utils.ptutils import *
from django.conf import settings

#3rd party modules
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

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


class Menu(MPTTModel):
        parent = TreeForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, db_index=True)
        page_template=models.ForeignKey(Page_Template,on_delete=models.CASCADE,help_text='Select Page Template');
        title = models.CharField(unique=True,max_length=100)
        toolstrip=models.CharField(max_length=255,blank=True)
        url = models.CharField(max_length=255, blank=True,editable=False)
        status = models.BooleanField(default=True)
        #lvl = models.PositiveIntegerField(default=0, blank=False, null=False)
        slug = models.SlugField(unique=True)
        image=models.ImageField(upload_to='menu/', blank=True, null=True)
        view_title=models.CharField(max_length=10, choices=VIEW_TITLE_CHOICE, default='Both')
        icon_class=models.CharField(max_length=100,blank=True, null=True,help_text='Enter the Font Awesome icon like fa fa-camera-retro fa-lg,fa fa-home')

        class Meta:
            db_table = "Menu"
            verbose_name = 'Menu'
            verbose_name_plural = 'Menu'
            

        class MPTTMeta:
            order_insertion_by = ('title',)

        def save(self, *args, **kwargs):
            
             #----------generate url field(copy url field from template)-----------
            if self.page_template:
                self.url=self.page_template.url
                
            #----------auto increment lavel lvl-----------
            # if self._state.adding: #only insert time work
            #     maxlvl= Menu.objects.all().aggregate(maxval=Max('lvl'))['maxval']  #field Name
            #     self.lvl= (int(maxlvl or 0)+1)

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

         
class Contact_Us(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length = 254)
    subject=models.CharField(max_length=200)
    content=models.TextField(max_length=500)
    is_read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
            verbose_name = 'Contact Us'
            verbose_name_plural = 'Contact Us'



    

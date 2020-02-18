from django.db import models
from django.conf import settings
import datetime
import uuid
from django.db.models import Max
from pytube.utils.ptutils import *

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('others', 'others'),
)

class Staff_Group(models.Model):
    name= models.CharField(max_length=50)
    is_active=models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
    lvl =  models.IntegerField('level',  editable=False)

   
    def save(self, *args, **kwargs):
        #-----------------slug------------
        if self.slug:  # edit
            if slugify(self.name) != self.slug:
                self.slug = generate_unique_slug(Staff_Group, self.name)
        else:  # create
            self.slug = generate_unique_slug(Staff_Group, self.name)

        #----------auto increment lavel-----------
        if self._state.adding: #only insert time work
            maxlvl= Staff_Group.objects.all().aggregate(maxval=Max('lvl'))['maxval']  #field Name
            print(maxlvl)
            self.lvl= (int(maxlvl or 0)+1)

        #----------super Execute------------
        super(Staff_Group, self).save(*args, **kwargs)

     #Count Group  of Staff
    def group_staff_count(self):
        return Staff.objects.filter(group=self).count()
    
    def __str__(self):
        return self.name

    #Met Descriptions
    class Meta:
        db_table = "pt_Staff_Group"
        verbose_name = 'staff-Group'
        verbose_name_plural = 'staff-Group'


 
# Create your models here.
class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,help_text='create user because one user is a one staff')
    display_name= models.CharField(max_length=50)
    gender= models.CharField(choices=GENDER_CHOICE,max_length=10, default='Male')
    dob= models.DateTimeField()
    edu_qualification= models.CharField("Educational Qualification",blank=True,max_length=50)
    designation= models.CharField("designation / Post",blank=True,max_length=50)
    opinion= models.TextField(max_length=500,blank=True)
    #email= present in user table
    contact_no= models.CharField(max_length=13,blank=True)
    description= models.TextField(max_length=500,blank=True)
    address=models.TextField(max_length=500,blank=True)

    staff_image = models.ImageField(upload_to='staff/images/', blank=True, null=True,help_text='Maximum file size allowed is 100kb')
    group=models.ForeignKey(Staff_Group, verbose_name="Group Name", on_delete=models.CASCADE)

    slug = models.SlugField(max_length=100, unique=True,default=uuid.uuid4,help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)



    @property
    def get_image_url(self):
         if self.staff_image and hasattr(self.staff_image, 'url'):
          return self.staff_image.url

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.display_name) != self.slug:
                self.slug = generate_unique_slug(Staff, self.display_name)
        else:  # create
            self.slug = generate_unique_slug(Staff, self.display_name)
        super(Staff, self).save(*args, **kwargs)

    def __str__(self):
        return self.display_name

    class Meta:
        db_table = "pt_Staff"
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'



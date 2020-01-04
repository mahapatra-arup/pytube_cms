from django.db import models
from django.template.defaultfilters import slugify
import datetime

AREA_CHOICE = (
    ('Rural', 'Rural'),
    ('Urban ', 'Urban '),
)
# ORG Details  Model
class Org_Details(models.Model):

    org_Name = models.CharField(max_length=200, unique=True)
    org_code=models.CharField(max_length=200,blank=True)
    at = models.CharField(max_length=200,blank=True)
    po = models.CharField(max_length=200,blank=True)
    block = models.CharField(max_length=200,blank=True)
    sub_division = models.CharField(max_length=200,blank=True)
    ps = models.CharField(max_length=200,blank=True)
    dist = models.CharField(max_length=200,blank=True)
    pin = models.CharField(max_length=200,blank=True)
    state_code = models.CharField(max_length=200,blank=True)
    area = models.CharField(max_length=100,choices=AREA_CHOICE, default='Rural',blank=True)
    map_url = models.TextField(max_length=500,blank=True)

    logo = models.ImageField(upload_to='org', blank=True, null=True)
    logo1 = models.ImageField(upload_to='org', blank=True, null=True)
    banner_logo = models.ImageField(upload_to='org', blank=True, null=True)

    slug = models.SlugField(unique=True,blank=True,editable=False)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organization'
   
    def __str__(self):
        return self.org_Name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.org_Name)
        super(Org_Details, self).save(*args, **kwargs)   

     
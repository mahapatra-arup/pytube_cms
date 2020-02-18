from django.db import models
from django.template.defaultfilters import slugify
import datetime

AREA_CHOICE = (
    ('Rural', 'Rural'),
    ('Urban ', 'Urban '),
)


class Org_SocialDetails(models.Model):
    name=models.CharField(max_length=100, unique=True)
    icon=models.CharField(max_length=100,blank=True,help_text='Icon like fa fa-twitter , fa fa-facebook, fa fa-google-plus, etc')
    css_class=models.CharField(max_length=100,help_text='like ico-twitter , ico-facebook, ico-googleplus, etc')
    activity=models.BooleanField()
    social_link=models.URLField(max_length=500,blank=True)

    class Meta:
        verbose_name = 'Org Social'
        verbose_name_plural = 'Org Social'
   
    def __str__(self):
        return self.name


class Org_ContactNo(models.Model):
    name=models.CharField(max_length=100)
    ph=models.CharField(max_length=13, unique=True)
    def __str__(self):
        return self.name+' - '+self.ph
    
    class Meta:
        verbose_name = 'Org Contacts'
        verbose_name_plural = 'Org Contacts'

class Org_UsefulLinks(models.Model):
    title=models.CharField(max_length=100)
    links=models.URLField()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Useful Links'
        verbose_name_plural = 'Useful Links'

# ORG Details  Model
class Org_Details(models.Model):
    org_name = models.CharField(max_length=200, unique=True)
    org_code=models.CharField(max_length=200,blank=True)
    at = models.CharField(max_length=200,blank=True)
    po = models.CharField(max_length=200,blank=True)
    block = models.CharField(max_length=200,blank=True)
    sub_division = models.CharField(max_length=200,blank=True)
    ps = models.CharField(max_length=200,blank=True)
    dist = models.CharField(max_length=200,blank=True)
    pin = models.IntegerField("ZIP / Postal code",blank=True)
    state = models.CharField(max_length=200,blank=True)
    state_code = models.CharField(max_length=200,blank=True)
    country =models.CharField(max_length=200,blank=True)
    area = models.CharField(max_length=100,choices=AREA_CHOICE, default='Rural',blank=True)
    map_url = models.TextField(max_length=500,blank=True)

    logo = models.ImageField(upload_to='org', blank=True, null=True)
    logo1 = models.ImageField(upload_to='org', blank=True, null=True)
    banner_logo = models.ImageField(upload_to='org', blank=True, null=True)
   

    website=models.URLField(max_length=200,blank=True)
    email=models.EmailField( max_length=254,blank=True)
    fax=models.CharField(max_length=50,blank=True)
    contact_no= models.ManyToManyField(Org_ContactNo,max_length=100, blank=True,related_name='rel_Org_ContactNo')
    social_details=models.ManyToManyField(Org_SocialDetails,blank=True,null=True)
    useful_link=models.ManyToManyField(Org_UsefulLinks,blank=True,null=True)
    slug = models.SlugField(unique=True,blank=True,editable=False)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organization'
   
    def __str__(self):
        return self.org_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.org_name)
        super(Org_Details, self).save(*args, **kwargs)   

     
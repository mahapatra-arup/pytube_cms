from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.
from django.shortcuts import reverse


from django.db.models.signals import pre_save
from pytube.utils.ptutils import generate_unique_slug
from versatileimagefield.fields import VersatileImageField


LABEL_COLOR_CHOICES = (
    ('primary', 'primary'),
    ('secondary', 'secondary'),
    ('danger', 'danger')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

# AVAILABILITY_PRODUCT = (
#     ('S', 'In Stock'),
#     ('0', 'Out Of Range')
# )

class ProductImage(models.Model):
    name = models.CharField(max_length=100, null=False)
    photo = models.ImageField(upload_to='shop/product/%Y/%m',null=True, blank=True)
    
    class Meta:
        db_table = "ProductImage"
        verbose_name = 'Product Images'
        verbose_name_plural = 'Product Images'

    @property
    def get_image_url(self):
         if self.photo and hasattr(self.photo, 'url'):
          return self.photo.url

    def __str__(self):
         return self.name


class Item_Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    background_image = VersatileImageField(
        upload_to="shop/Item_Category", blank=True, null=True
    )
    background_image_alt = models.CharField(max_length=128, blank=True)
    parent= models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField()

    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Item_Category,  on_delete=models.CASCADE)

    label = models.CharField(max_length=15)
    label_color = models.CharField(choices=LABEL_COLOR_CHOICES, max_length=10)

    stock =  models.IntegerField()

    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    is_active=models.BooleanField(default=True)

    thumbnail_img=models.ImageField('Thumnail Image',upload_to="shop/product/%Y/%m",blank=True)
    product_image = models.ManyToManyField(ProductImage, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    verified=models.BooleanField(default=True)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    meta_keywords = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

     ###get_image_url
    @property
    def get_thumb_img_url(self):
         if self.thumbnail_img and hasattr(self.thumbnail_img, 'url'):
          return self.thumbnail_img.url


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_received = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    add comment
    
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"

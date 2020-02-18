from django.db import models
import datetime

# Create your models here.
# #document Upload----------------------->
# class Document_File(models.Model):
#     upload = models.FileField(upload_to="uploads/document/%Y/%m/%d/")
#     created_on = models.DateTimeField(default=datetime.datetime.now)
#     is_image = models.BooleanField(default=True)
#     thumbnail = models.ImageField( upload_to="uploads/document/%Y/%m/%d/",blank=True, null=True)

#     def __str__(self):
#         return self.date_created    

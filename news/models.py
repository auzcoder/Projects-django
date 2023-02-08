
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

# Yangiliklar uchun postlar qismi
class New (models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    full_info =RichTextField('text')
    header_images = models.ImageField(default='news.png', upload_to = 'uploads/news/images', blank=True)
    category = models.ForeignKey()
    #upload_to = 'news/image'
    date = models.DateTimeFieldField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                               )
   

    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

# Kategoriya yaratish qismi
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Yangiliklar uchun postlar qismi
class New (models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    full_info = RichTextField()
    header_images = models.ImageField(default='news/images/news.jpg', upload_to='news/images', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # upload_to = 'news/image'
    date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                               )

    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

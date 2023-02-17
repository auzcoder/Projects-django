
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone


# Create your models here.

#Publish manager uchun model
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = New.Status.Published)

# Kategoriya yaratish qismi uchun model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name

# Yangiliklar uchun postlar qismi bo'yicha model
class New (models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    full_info = RichTextField()
    header_images = models.ImageField(default='news/images/news.jpg', upload_to='news/images', blank=True)
    category = models.ManyToManyField(Category, null=False, blank=False)
    sub_category = models.ManyToManyField(SubCategory, null=True, blank=True)
    # upload_to = 'news/image'
    date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                               )
    object = models.Manager() #Default manager
    published = PublishedManager()

    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])


#Contact bo'limi uchun model
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=1500)

    def __str__(self):
        return self.email

from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

# Yangiliklar uchun postlar qismi
class New (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    full_info =RichTextField('text', config_name='extends')
    header_images = models.ImageField(default='news.png', blank=True)
    date = models.DateField(default=datetime.now, blank=True)

    # userid = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

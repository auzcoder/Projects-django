# Generated by Django 4.1.6 on 2023-02-04 06:07

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='full_info',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='text'),
        ),
    ]

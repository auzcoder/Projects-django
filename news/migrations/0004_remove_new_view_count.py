# Generated by Django 4.1.7 on 2023-03-06 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_new_view_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='view_count',
        ),
    ]

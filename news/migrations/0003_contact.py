# Generated by Django 4.1.6 on 2023-02-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_new_managers_remove_new_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=1500)),
            ],
        ),
    ]

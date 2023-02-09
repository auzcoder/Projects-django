from django.contrib import admin
from .models import New, Category

# Register your models here.

# admin.site.register(New)
@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["id", 'name', 'category', 'created_at', 'update_at', 'status']
    list_filter = ['status', 'category', 'created_at', "update_at"]
    list_editable = ['status', 'category']
    list_display_links = ['name', 'id']
    date_hierarchy = 'date'
    search_fields = ['name', 'description']
    ordering = ['status', 'date']

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
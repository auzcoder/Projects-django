from django.contrib import admin
from .models import New, Category, SubCategory

# Register your models here.

# admin.site.register(New)
@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["id", 'name', 'created_at', 'update_at', 'status']
    list_filter = ['status', 'sub_category', 'created_at', "update_at"]
    list_editable = ['status']
    list_display_links = ['name', 'id']
    date_hierarchy = 'date'
    search_fields = ['name', 'description']
    ordering = ['status', 'date']


class SubCategoryInlineAdmin(admin.TabularInline):
    model = SubCategory

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    inlines = [SubCategoryInlineAdmin]
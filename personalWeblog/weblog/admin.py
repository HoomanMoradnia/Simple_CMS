from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {
            'fields': ['title', 'author', 'status', 'slug', 'image']
        }),
        ('Content', {
            'fields': ['content']
        }),
        ('Date information', {
            'fields': ['created_at', 'updated_at']
        }),
    ]
    readonly_fields = ['created_at', 'updated_at', 'slug']
    list_display = ['title', 'author', 'created_at', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'content', 'author__username']
    list_editable = ['status']
    list_per_page = 10
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

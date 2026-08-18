from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'is_published')
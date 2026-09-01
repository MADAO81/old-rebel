from django.contrib import admin
from .models import Bike, ComparisonArticle, ContactMessage

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'years')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ComparisonArticle)
class ComparisonArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read',)
    readonly_fields = ('name', 'email', 'message', 'created_at')
from django.contrib import admin
from .models import Bike, ComparisonArticle

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'years')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ComparisonArticle)
class ComparisonArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
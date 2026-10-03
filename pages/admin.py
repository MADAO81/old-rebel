from django.contrib import admin
from .models import Bike, ComparisonArticle, ContactMessage, CookieConsent


# @admin.register(Bike)
# class BikeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'code', 'years')
#     prepopulated_fields = {'slug': ('name',)}


@admin.register(ComparisonArticle)
class ComparisonArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read',)
    readonly_fields = ('name', 'email', 'message', 'created_at')


@admin.register(CookieConsent)
class CookieConsentAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'consent_given', 'created_at')
    list_filter = ('consent_given', 'created_at')
    readonly_fields = ('ip_address', 'user_agent', 'consent_given', 'created_at')
    search_fields = ('ip_address',)

    def has_add_permission(self, request):
        return False
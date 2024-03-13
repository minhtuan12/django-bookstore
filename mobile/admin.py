from django.contrib import admin

from mobile.models import Mobile


# Register your models here.

@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'price', 'image']

    list_display_links = ['name', 'brand', 'price', 'image']

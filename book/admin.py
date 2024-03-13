from django.contrib import admin

from book.models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'description', 'sku', 'price', 'old_price', 'image', 'quantity',
                    'meta_keywords']

    list_filter = ['status']

    list_display_links = ['title', 'author', 'slug', 'description', 'sku', 'price',
                          'old_price', 'image', 'quantity', 'meta_keywords']

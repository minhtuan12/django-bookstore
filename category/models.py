from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(default = '', null = True, blank = True)
    slug = models.SlugField(
        max_length = 50,
        unique = True,
        help_text = 'Unique value for product page URL, created from name.'
    )
    meta_keywords = models.CharField(
        max_length = 255,
        help_text = 'Comma-delimited set of SEO keywords for meta tag',
        default = '', null = True, blank = True
    )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(default = None, null = True, blank = True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    ordering = ['-created_at']

    def __str__(self):
        return self.name

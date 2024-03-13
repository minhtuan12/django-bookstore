from django.db import models

from category.models import Category

# Create your models here.

BOOK_STATUS = {
    'INACTIVE': 0,
    'ACTIVE': 1
}


class Book(models.Model):
    title = models.CharField(max_length = 255, unique = True)
    author = models.CharField(max_length = 255)
    description = models.TextField(null = True, blank = True)
    slug = models.SlugField(max_length = 255, unique = True,
                            help_text = 'Unique value for product page URL, created from name.')
    sku = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    old_price = models.DecimalField(max_digits = 9, decimal_places = 2, default = None, null = True, blank = True)
    image = models.CharField(max_length = 50, null = True, blank = True, default = '')
    status = models.BooleanField(default = BOOK_STATUS['ACTIVE'])
    quantity = models.IntegerField()
    meta_keywords = models.CharField(max_length = 255, help_text = 'Comma-delimited set of SEO keywords for meta tag', null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(default = None, null = True, blank = True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'books'
        verbose_name_plural = 'Books'

    ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.price != self.old_price:
            self.old_price = self.price
        super().save(*args, **kwargs)

from djongo import models


# Create your models here.

class Mobile(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length = 100)
    brand = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    image = models.CharField(max_length = 100, default = "")

    class Meta:
        db_table = 'mobiles'
        verbose_name_plural = 'Mobiles'

    ordering = ['-created_at']

    def __str__(self):
        return self.name

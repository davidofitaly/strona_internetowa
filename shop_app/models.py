from django.db import models

# Create your models here.

class Producers(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'


class Categories(models.Model):

    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Products(models.Model):
    category = models.ForeignKey(Categories, null=True, blank=False, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producers, null=True, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


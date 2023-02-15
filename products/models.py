from django.db import models
import uuid
from general.models import BaseModel

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True, null=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'products_product_category'
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.title

class Product(BaseModel):
    name = models.CharField(max_length=128, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    product_category = models.ForeignKey('products.ProductCategory', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        db_table = 'products_product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    product = models.ForeignKey('products.Product', on_delete=models.RESTRICT, blank=True, null=True)

    class Meta:
        db_table = 'products_product_image'
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        
    def __str__(self):
        return self.title

from django.contrib import admin
from products.models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description')
    search_fields = ('name', 'id')
admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_added')
admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'product')
admin.site.register(ProductImage, ProductImageAdmin)

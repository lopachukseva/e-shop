from django.contrib import admin
from products.models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductCategory)
admin.site.register(Product)

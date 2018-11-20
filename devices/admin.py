from django.contrib import admin
from devices.models import Product, ProductImage, \
    ProduCategory


class ProductImageInLine(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    inlines = [
        ProductImageInLine
    ]

class ProduCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}


admin.site.register(Product, ProductAdmin)
admin.site.register(ProduCategory, ProduCategoryAdmin)
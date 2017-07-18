from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'cost', 'brand']


admin.site.register(Product, ProductAdmin)

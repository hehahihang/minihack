from django.contrib import admin
from .models import Product, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'stock',
    )
    search_fields = (
        'title',
        'price',
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'scores',
        'product',
    )
    search_fields = (
        'socres',
    )


# Register your models here.

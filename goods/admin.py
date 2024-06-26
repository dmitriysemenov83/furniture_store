from django.contrib import admin

from goods.models import Categories, Products


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'discount', 'quantity', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('discount',)
    search_fields = ('name', 'description',)
    list_filter = ('discount', 'category', 'price',)
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
    ]


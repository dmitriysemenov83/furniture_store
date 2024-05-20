from django.contrib import admin

from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'image', 'price', 'discount', 'quantity', 'category')
    prepopulated_fields = {'slug': ('name',)}

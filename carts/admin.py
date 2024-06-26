from django.contrib import admin

from carts.models import Cart


class CartInline(admin.TabularInline):
    model = Cart
    fields = ('product', 'quantity', 'created_at',)
    search_fields = ('product', 'quantity', 'created_at',)
    readonly_fields = ('created_at',)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user_display', 'product_display', 'quantity', 'created_at',)
    list_filter = ('created_at', 'user', 'product__name',)

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'
    user_display.short_description = 'Пользователь'

    def product_display(self, obj):
        return str(obj.product.name)
    product_display.short_description = 'Товар'

from django.contrib import admin

from carts.admin import CartInline
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    fields = [
        # 'username',
        'first_name',
        'last_name',
        'email',
        'image',
        'is_active',
        'is_staff',
        ('date_joined', 'last_login'),
        'groups',
        'user_permissions'
    ]

    inlines = (CartInline,)

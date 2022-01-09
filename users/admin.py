from .models import User
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class AdminUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'phonenumber')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'phonenumber', 'is_staff',)
    search_fields = ('username', 'email',)
    ordering = ('date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, AdminUserAdmin)
admin.site.unregister(Group)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.internal.rest.admin_user.db.models import AdminUser


@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    pass

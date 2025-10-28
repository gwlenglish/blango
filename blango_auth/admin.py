from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from blango_auth.models import User


@admin.register(User)
class BlangoUserAdmin(UserAdmin):
    # Field layout when viewing/editing a user
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Field layout when adding a new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    # Columns shown in user list
    list_display = ("email", "first_name", "last_name", "is_staff")

    # Searchable fields
    search_fields = ("email", "first_name", "last_name")

    # Default sort order
    ordering = ("email",)

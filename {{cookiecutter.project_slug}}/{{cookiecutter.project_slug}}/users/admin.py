from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from {{ cookiecutter.project_slug }}.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


# changed for django 2.1 see: https://github.com/pydanny/cookiecutter-django/issues/1654
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ["email", "is_active", "is_staff", "is_superuser", "date_joined"]
    list_filter = ["groups", "is_active", "is_staff", "is_superuser"]
    search_fields = ["email"]
    ordering = ["-date_joined"]

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, Team, Task


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'users'


class UserAdmin(BaseUserAdmin):
    inlines = (UserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Task)

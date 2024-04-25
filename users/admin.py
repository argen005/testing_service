from django.contrib import admin

from users.models import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active')
    list_display_links = list_display
    search_fields = ('email',)
    exclude = ('password', 'groups', 'user_permissions')


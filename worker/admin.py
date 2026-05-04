from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from worker.models import CustomWorker


# Register your models here.
@admin.register(CustomWorker)
class WorkerAdminOverload(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')

    def get_groups(self, obj):
        """Get all group objects."""
        return ', '.join([group.name for group in obj.groups_all()])

    get_groups.short_description = "Groups"

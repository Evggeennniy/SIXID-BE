from django.contrib import admin
from todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'title',  'priority', 'deadline', 'is_active')
    list_filter = ('priority', 'is_active')
    search_fields = ('title', 'user__username')

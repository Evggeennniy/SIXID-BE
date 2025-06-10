from django.contrib import admin
from todos.models import Task, SubTask


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 0
    fields = ('title', 'is_active')
    show_change_link = True


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active', 'title',  'priority', 'deadline')
    list_filter = ('priority', 'is_active')
    search_fields = ('title', 'user__username', 'id')
    inlines = [SubTaskInline]

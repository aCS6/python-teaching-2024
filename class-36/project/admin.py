from django.contrib import admin
from .models import Project, Task, Tag, Location

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1  # Number of empty forms to display

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')  # Adjust fields as needed
    list_filter = ('created_by', 'tags')  # Filters on the right side
    search_fields = ('name', 'description')  # Searchable fields
    inlines = [TaskInline]  # Inline task creation/editing

    def created_at(self, obj):
        return obj.created_at
    created_at.admin_order_field = 'created_at'  # Allow sorting

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'project', 'created_by')  # Adjust fields as needed
    list_filter = ('completed', 'project', 'created_by')  # Filters on the right side
    search_fields = ('title', 'project__name')  # Searchable fields

# Register the models with the custom admin classes
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Tag)
admin.site.register(Location)

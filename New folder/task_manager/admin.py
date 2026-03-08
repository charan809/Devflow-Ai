from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Columns shown in the admin list
    list_display = ('title', 'display_complexity', 'estimated_hours', 'created_at')
    
    # Sidebar filters
    list_filter = ('complexity', 'created_at')
    
    # Search functionality
    search_fields = ('title', 'description')
    
    # Newest tasks appear at the top
    ordering = ('-created_at',)

    # Makes complexity look professional with stars
    def display_complexity(self, obj):
        stars = "⭐" * obj.complexity
        return f"{stars} ({obj.complexity}/5)"
    
    display_complexity.short_description = 'Complexity'
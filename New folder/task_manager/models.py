from django.db import models

class Task(models.Model):
    # Core Task Details
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Complexity input for the ML model (1-5)
    complexity = models.IntegerField(default=1)
    
    # AI Generated Fields
    # Storing hours as a float for precision
    estimated_hours = models.FloatField(null=True, blank=True)
    
    # Storing sub-tasks as a text block (can be parsed in templates)
    sub_tasks = models.TextField(null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
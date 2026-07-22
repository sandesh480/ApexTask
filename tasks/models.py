from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add= True)
    due_date = models.DateTimeField(null= True, blank=True)
    is_completed = models.BooleanField(default= False)

    def __str__(self):
        return self.title
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        # Automatically orders tasks so the newest tasks appear at the top
        ordering = ['-id']

    def __str__(self):
        # Tells Django to display the actual title instead of "Task object (1)"
        return self.title
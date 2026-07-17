from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Task

def task_list(request):
    # Fetch all tasks from our SQLite database
    all_tasks = Task.objects.all()
    
    # Send them to our HTML template
    return render(request, 'tasks/task_list.html', {'tasks': all_tasks})
from django.urls import path
from . import views

urlpatterns = [
    # Maps the root URL of this app to our task_list view
    path('', views.task_list, name='task_list'),
]
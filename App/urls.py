from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # Add Task
    path('addTask/', views.addTask, name='addTask'),
    # Move to Done
    path('done/<int:pk>/', views.done, name='done'),
    # Return to Todo List
    path('back/<int:pk>/', views.back, name='back'),
    #Edit Task
    path('edit/<int:pk>/', views.edit, name='edit'),
    # Delete Task
    path('delete/<int:pk>/', views.delete, name='delete')
]


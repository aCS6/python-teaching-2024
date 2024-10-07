from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.todo_list, name='todo_list'),
    path('create/',view=views.create_todo, name='todo_create' ),
    path('update/<int:pk>/', view=views.update_todo, name='todo_update'),
    path('delete/<int:pk>/', view=views.delete_todo, name='delete_todo'),
]

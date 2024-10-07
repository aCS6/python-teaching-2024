from django.urls import path
from . import function_views
from . import class_view

urlpatterns = [
    # path("todos/", function_views.todos ,name="todos"),
    # path("todos/<int:pk>/", function_views.todo_details ,name="todos-details"),

    path("todos/", class_view.TodoListCreate.as_view() ,name="todos"),
    path("todos/<int:pk>/", class_view.TodoRetrieveUpdateDestroy.as_view() ,name="todos-details"),
]
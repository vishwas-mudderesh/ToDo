from django.urls import path
from . import views
urlpatterns = [
    #add task
    path('addTask/',views.addTask,name='addTask'),
    # markdone
    path('mark_as_done/<int:pk>/',views.mark_as_done,name="mark_as_done"),
    # markundone
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name="mark_as_undone"),
    # edit 
    path("edit_task/<int:pk>",views.edit_task,name='edit_task'),
    #delete
    path("delete_task/<int:pk>/",views.delete_task,name="delete_task"),
]
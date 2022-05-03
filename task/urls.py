from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home-task"),
    path('update-task/<int:pk>/', views.updateTask, name="update-task"),
    path('delete-task/<int:pk>/', views.deleteTask, name="delete-task"),
]

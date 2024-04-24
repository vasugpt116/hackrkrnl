from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_task/', views.add_task, name='add_task'),
    path('users/', views.list_users, name='list_users'),
    path('tasks/', views.list_tasks, name='list_tasks'),
    path('export/', views.export_to_excel, name='export_to_excel'),
]
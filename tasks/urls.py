from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name= 'home'),
    path('update/<task_id>/', views.update_form , name='update'),
    path('delete/<task_id>/', views.delete_task , name='delete'),


]

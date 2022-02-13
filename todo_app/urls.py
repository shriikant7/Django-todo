from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<id>', views.deletetodo, name='delete'),
    path('mark/<id>', views.marktodo, name='marktodo'),
    path('unmark/<id>', views.unmarkedtodo, name='unmarktodo'),
    path('add', views.addtodo, name='addtodo'),
]

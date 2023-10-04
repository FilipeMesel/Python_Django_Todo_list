"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-todos/', views.register_todos, name='register_todos'),
    path('todos/', views.list_todos, name='list_todos'),
    path('atualizar-status-todo/<int:todo_id>/', views.atualizar_status_todo, name='atualizar_status_todo'),
    path('excluir-todo/<int:todo_id>/', views.excluir_todo, name='excluir_todo'),
]

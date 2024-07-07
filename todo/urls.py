from django.contrib import admin

from django.urls import path, include

from todo.views import index, contact, create, mark_as_done, delete_task, edit

urlpatterns = [
    path("", index), 
    path("contact", contact),
    path("create", create),
    path("task/<pk>/mark", mark_as_done),
    path("task/<pk>/delete", delete_task),
    path("task/<pk>/edit", edit)
    ]

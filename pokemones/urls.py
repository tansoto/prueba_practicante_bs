from django.urls import path
from .views import list_tasks, CRUD

urlpatterns = [
    path('', list_tasks),
    path('CRUD/', CRUD)
]

from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . views import ToDoViewSet


router = routers.DefaultRouter()
router.register('todos', ToDoViewSet, 'todo-list')

urlpatterns = [
    path('', include(router.urls))
]
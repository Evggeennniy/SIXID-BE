from todos.views import TaskViewSet, SubTaskViewSet
from rest_framework.routers import DefaultRouter
# from django.urls import path

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')
router.register(r'subtasks', SubTaskViewSet, basename='subtasks')

urlpatterns = router.urls

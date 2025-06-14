from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('normal', 'Обычно'),
        ('important', 'Важно'),
        ('urgent', 'Срочно'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=64)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='normal',
    )
    deadline = models.DateField(
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Task {self.title}"


class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Subtask {self.title}"

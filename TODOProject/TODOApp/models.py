from django.db import models

# Create your models here.

class Todo(models.Model):
    desc = models.TextField()
    isCompleted = models.BooleanField(default=False)
    completeAt = models.DateField(null=True)
    taskCompletedDate = models.DateField(null=True)
    createdAt = models.DateField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Модель проектов
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
#Модель статусов для задач
class TaskStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Модель задач
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_date= models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    reminder = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey(TaskStatus, null=True, blank=True, on_delete=models.CASCADE)
    task_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
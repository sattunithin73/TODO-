from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)

# to store the tasks which the user as completed 
class CompleteModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)

#to store the delete task 
class TrashModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
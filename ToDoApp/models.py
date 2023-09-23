from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class ToDos(models.Model):
    STATUS = [('completed', "Completed"), ('pending', "Pending")]
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS)
    due_date = models.DateField()


from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')])

class Employee(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

class Tool(models.Model):
    name = models.CharField(max_length=255)
    condition = models.CharField(max_length=50)
    assigned_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

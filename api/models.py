from django.db import models
from account.models import User

# Create your models here.

class Holiday(models.Model):
    name = models.CharField(max_length=100)
    holiday_date = models.DateField()
    no_of_days = models.IntegerField()

    def __str__(self):
        return self.name


class Compensation(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    ctc = models.CharField(max_length=50)
    basic = models.CharField(max_length=50)
    hra = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=200)
    employee = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    

class Client(models.Model):
    name = models.CharField(max_length=100)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.name
    
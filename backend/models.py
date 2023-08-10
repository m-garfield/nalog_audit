from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    father_name = models.CharField(max_length=50, null=False)
    position_work = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=False)


# Create your models here.

from django.db import models

# Create your models here.

class Donors(models.Model):
    D_name=models.CharField(max_length=100)
    D_age=models.IntegerField()
    D_blood=models.TextField()
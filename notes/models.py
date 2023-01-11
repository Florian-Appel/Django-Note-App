from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

class Notes(models.Model):
    title = models.CharField(max_length=30)
    note = models.CharField(max_length=100)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True, null=True)
    category = models.CharField(max_length=20)
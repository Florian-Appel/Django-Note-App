from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20 , default=None, blank=True, null=True)

class Notes(models.Model):

    CATEGORIES = (
        ("GEN", "General"),
        ("PRI", "Privat"),
        ("PRO", "Professional"),
        ("OTH", "Other"),
    )

    title = models.CharField(max_length=30, default=None, blank=True, null=True)
    note = models.CharField(max_length=100, default=None, blank=True, null=True)
    #category = models.CharField(max_length=20, choices=CATEGORIES, default=None, blank=True, null=True)
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class form(models.Model):
    name = models.CharField(max_length=200)
    emailid = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    reviews = models.TextField()
    #number =
    def __str__(self):
        return self.name

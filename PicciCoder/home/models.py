from os import name
from django.db import models

class Contact(models.Model):
     sno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=111)
     email = models.CharField(max_length=111)

     content = models.TextField()
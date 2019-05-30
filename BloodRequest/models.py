from django.db import models

# Create your models here.
class requests(models.Model):
    name = models.CharField(max_length=50)
    district = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    primaryContact = models.IntegerField()
    secondaryContact = models.IntegerField()
    email = models.EmailField()
    bloodGroup = models.CharField(max_length=3)
    description = models.TextField()
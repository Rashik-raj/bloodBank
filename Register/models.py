from django.db import models

# Create your models here.
class Donors(models.Model):
    firstName = models.CharField(max_length=15)
    middleName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    district = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    primaryContact = models.IntegerField()
    secondaryContact = models.IntegerField()
    email = models.EmailField()
    bloodGroup = models.CharField(max_length=3)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.firstName + " " + self.bloodGroup
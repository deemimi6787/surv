from django.db import models
from datetime import datetime,date

class Register(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    idNo = models.IntegerField()
    phoneNo = models.BigIntegerField()
    email = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.userName + ' | ' + self.password + ' | '

class Mutation(models.Model):
    emp = models.ForeignKey(Register, on_delete=models.CASCADE)
    county = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    idNumber = models.CharField(max_length=100)
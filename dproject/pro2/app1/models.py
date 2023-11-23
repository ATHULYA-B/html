from django.db import models

# Create your models here. 
class Emp(models.Model): 
    Name=models.CharField(max_length=25)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Place=models.CharField(max_length=40)


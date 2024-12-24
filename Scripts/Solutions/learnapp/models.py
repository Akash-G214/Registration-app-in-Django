from django.db import models

# Create your models here.
class Person(models.Model):
    FirstName=models.CharField(max_length=100,null=True)
    LastName=models.CharField(max_length=100,null=True)
    Email=models.EmailField(max_length=100,null=True)
    Password=models.CharField(max_length=100,null=True)
    Repassword=models.CharField(max_length=100,null=True)
    Phone=models.CharField(max_length=100,null=True)
     
    class Meta:
        db_table='Person'
    def __str__ (self):
        return self.Email
  

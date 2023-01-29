from django.db import models
#Here we have to create models fields for the Database.
#Create the Models as per your Requirement, we have create below fields to perform a basic CRUD Operation for an Ecommerce.
class Ecommerce(models.Model):
    name=models.CharField(max_length=50)
    categeory=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    details=models.TextField(max_length=100,blank=True)
    image=models.ImageField(upload_to='myimage',blank=True)#we have added "Blank" attribute, so if anyone can update or Insert a data without image.


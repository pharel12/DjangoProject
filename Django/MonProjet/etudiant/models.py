from django.db import models

# Create your models here.
class User(models.Model):
    image = models.ImageField(upload_to='etudiant/images/')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    

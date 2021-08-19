from django.db import models

# Create your models here.

# For contact form, includes individual's name, email, and comments.
class Contact(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70, unique=True)
    comments = models.TextField(max_length=100)

class Characters(models.Model):
    image = models.ImageField(null=False, blank=False, 
        upload_to="characters/")

    name = models.CharField(max_length=70, default='Character - ') 

    def __str__(self):
        return self.name

class Graphics(models.Model):
    image = models.ImageField(null=False, blank=False, 
        upload_to="graphics/")

    name = models.CharField(max_length=70, default='Graphic - ')

    def __str__(self):
        return self.name

class Illustrations(models.Model):
    image = models.ImageField(null=False, blank=False, 
        upload_to="illustrations/")

    name = models.CharField(max_length=70, default='Illustration - ')

    def __str__(self):
        return self.name

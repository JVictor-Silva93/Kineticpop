from django.db import models

# Create your models here.

# For contact form, includes individual's name, email, and comments.
class Contact(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70, unique=True)
    comments = models.TextField(max_length=100)

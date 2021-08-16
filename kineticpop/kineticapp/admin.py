from django.contrib import admin
from .models import Contact

# Register your models here.

# importing Contact from the models.py, and then creating a Contact dashboard in the admin allows us access to form information submitted in the contacts page.
admin.site.register(Contact)

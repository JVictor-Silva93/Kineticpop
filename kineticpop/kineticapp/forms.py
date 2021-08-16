from django import forms
from .models import Contact


#ModelForm allows the HTML form to save data to a database
#class Meta connects the form to our Contact model via model attribute
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

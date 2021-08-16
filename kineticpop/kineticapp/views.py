from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, "kineticapp/index.html")

# if statement in contact causes a reaction. if someone submits a valid form, the form info will be stored.
# if there is a post request (which it is set up to be so), and submitted/valid -- form will save and return success page.
# form.save() runs Django's built in form verifying function.
def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, "kineticapp/success.html")
        else:
            return HttpResponse("invalid")

    context = {"form": form}
    return render(request, "kineticapp/contact.html", context)

def success(request):
    return render(request, "kineticapp/success.html")

def graphics(request):
    return render(request, "kineticapp/graphics.html")

def illustrations(request):
    return render(request, "kineticapp/illustrations.html")

def characters(request):
    return render(request, "kineticapp/characters.html")

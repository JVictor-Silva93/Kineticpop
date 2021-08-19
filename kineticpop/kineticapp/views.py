from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Characters, Graphics, Illustrations

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

# create a objects.all() to obtain all the objects uploaded to each model/admin section (i.e. - Characters, Illustrations, Graphics)
# context allows you to plugin to the return render
def graphics(request):
    graphics = Graphics.objects.all()
    context = {'graphics': graphics}
    return render(request, "kineticapp/graphics.html", context)

def illustrations(request):
    illustrations = Illustrations.objects.all()
    context = {'illustrations': illustrations}
    return render(request, "kineticapp/illustrations.html", context)

def characters(request):
    characters = Characters.objects.all()
    context = {'characters': characters}
    return render(request, "kineticapp/characters.html", context)

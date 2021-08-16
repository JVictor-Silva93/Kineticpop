from django.urls import path
from kineticapp import views

# TEMPLATE TAGGING

app_name = 'kineticapp'

urlpatterns = [
    path("illustrations", views.illustrations, name="illustrations"),
    path("characters", views.characters, name="characters"),
    path("graphics", views.graphics, name="graphics"),
    path("contact", views.contact, name="contact"),
    path("success", views.success, name="success"),
    path('', views.index, name='index'),
]
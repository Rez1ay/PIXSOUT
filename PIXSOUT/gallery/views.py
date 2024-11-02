from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Screenshot


class Gallery(ListView):
    model = Screenshot
    template_name = 'gallery/gallery.html'
    context_object_name = 'screenshots'

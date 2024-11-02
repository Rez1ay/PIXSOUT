from django.shortcuts import render
from django.views.generic import TemplateView


class Download(TemplateView):
    template_name = 'download/download.html'

from django.shortcuts import render
from django.views.generic import TemplateView


class Donate(TemplateView):
    template_name = 'donate/donate.html'

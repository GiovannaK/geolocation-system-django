from django.shortcuts import render
from .models import Location
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'location/index.html'



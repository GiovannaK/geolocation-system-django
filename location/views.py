from django.shortcuts import render, get_object_or_404
from .models import Location
# from django.views.generic import TemplateView
from .forms import LocationForm

""" class HomeView(TemplateView):
    template_name = 'location/index.html' """

def calculate_distance(request):
    obj = get_object_or_404(Location, id=1)
    form = LocationForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.destination = form.cleaned_data.get('destination') 
        instance.location = 'Cascavel'
        instance.distance = 5000.00
        instance.save()
    else:
        form = LocationForm()
        
    context = {
        'distance': obj,
        'form': form,
    }
    return render(request, 'location/index.html', context)



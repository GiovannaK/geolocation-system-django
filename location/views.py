from django.shortcuts import render, get_object_or_404
from .models import Location
from .forms import LocationForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo

def calculate_distance(request):
    obj = get_object_or_404(Location, id=1)
    form = LocationForm(request.POST or None)
    geolocator = Nominatim(user_agent='location')

    ip = '72.14.207.99'
    country, city, lat, lon = get_geo(ip)
    location = geolocator.geocode(city)

    l_lat = lat
    l_lon = lon
    point_A = (l_lat, l_lon)
    
    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination') 
        destination = geolocator.geocode(destination_)
        d_lat = destination.latitude
        d_lon = destination.longitude

        point_B = (d_lat, d_lon)
        distance = round(geodesic(point_A, point_B).km, 2)
        
        instance.location = location
        instance.distance = distance
        instance.save()
    else:
        form = LocationForm()

    context = {
        'distance': obj,
        'form': form,
    }
    return render(request, 'location/index.html', context)



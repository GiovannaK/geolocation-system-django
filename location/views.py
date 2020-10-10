from django.shortcuts import render, get_object_or_404
from .models import Location
from .forms import LocationForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coord, get_zoom, get_ip
import folium


def calculate_distance(request):
    distance = None
    destination = None
    location = None
    form = LocationForm(request.POST or None)
    geolocator = Nominatim(user_agent='location')

    ip = get_ip(request)
    
    country, city, lat, lon = get_geo(ip)
    location = geolocator.geocode(city)

    # location coords
    l_lat = lat
    l_lon = lon
    point_A = (l_lat, l_lon)

    # initial map
    m = folium.Map(width=800, height=400, 
        location=get_center_coord(l_lat, l_lon), 
        zoom_start=8
    )
    
    folium.Marker([l_lat, l_lon], tooltip='Clique aqui ver mais', 
        popup=city['city'], icon=folium.Icon(color='black')
    ).add_to(m)
    
    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination') 
        destination = geolocator.geocode(destination_)
        
        # destination coords
        d_lat = destination.latitude
        d_lon = destination.longitude

        point_B = (d_lat, d_lon)
        distance = round(geodesic(point_A, point_B).km, 2)
        
        # map modification
        m = folium.Map(width=800, height=400, 
            location=get_center_coord(l_lat, l_lon, d_lat, d_lon), 
            zoom_start=get_zoom(distance)
        )
        # locatio marker
        folium.Marker([l_lat, l_lon], tooltip='Clique aqui ver mais', 
            popup=city['city'], icon=folium.Icon(color='black')
        ).add_to(m)

        # destination marker
        folium.Marker([d_lat, d_lon], tooltip='Clique aqui ver mais', 
            popup=destination, icon=folium.Icon(color='purple', icon="cloud")
        ).add_to(m)

        #line route
        line = folium.PolyLine(locations=[point_A, point_B], 
            weight=2, color='blue'
        )

        m.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()
    else:
        form = LocationForm()

    m = m._repr_html_()
    
    context = {
        'distance': distance,
        'form': form,
        'map': m,
    }
    return render(request, 'location/index.html', context)



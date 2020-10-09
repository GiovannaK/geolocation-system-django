from django.urls import path
# from . views import HomeView
from . views import calculate_distance

app_name = 'location'

urlpatterns = [
    path('', calculate_distance, name='calculate_distance')    
]




from django.shortcuts import render

def home(request):
    return render(request, 'location/index.html')

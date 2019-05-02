from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests


# Create your views here.
def homepage(request):

    if request.method == 'POST':
       form = CityForm(request.POST)
       if form.is_valid():
          form.save()

    form= CityForm()

    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ac0c0e5de428e96b0231cac7541f980b"
    cities= City.objects.all()

    weather_info=[]
    for city in cities:
        r=requests.get(url.format(city)).json()
        city_weather={
               'id' : city.id,
               'city' : r['name'],
               'temperature' : r['main']['temp'],
               'description' : r['weather'][0]['description'],
               'icon' : r['weather'][0]['icon'],
               }
        weather_info.append(city_weather)


    context ={'weather_info':weather_info , 'form': form}

    return render(request,'weather_app/weather.html',context)

from django.urls import path
from django.conf.urls import url
from weather_app import views

urlpatterns =[
path('',views.homepage ,name='homepage')
]

from django.urls import path
from . import views

urlpatterns = [
    path('continent/', views.getContinent, name='continent'),
    path('continent/<int:pk>', views.getEachContinent),
    path('country/', views.getCountry, name='country'),
    path('country/<int:pk>', views.getEachCountry),
    path('country/add', views.addCountry, name='addcountry'),
    
]

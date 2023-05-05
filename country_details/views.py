from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Continent, Country
from . serializers import ContinentSerializer, CountrySerializer

def index(request):
    return render(request, 'index.html')


# Continent
@api_view(['GET'])
def getContinent(request):
    continent = Continent.objects.all()
    serializer = ContinentSerializer(continent, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEachContinent(request, pk):
    continent = Continent.objects.get(id=pk)
    serializer = ContinentSerializer(continent, many=False)
    return Response(serializer.data)

# Country

@api_view(['GET'])
def getCountry(request):
    country = Country.objects.all()
    serializer = CountrySerializer(country, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEachCountry(request, pk):
    country = Country.objects.get(id=pk)
    serializer = CountrySerializer(country, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCountry(request):
    serializer = CountrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

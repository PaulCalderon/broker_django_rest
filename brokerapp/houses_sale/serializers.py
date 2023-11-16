#from .serializers import HouseSerializer
from rest_framework import serializers
from .models import HouseList


class HouseSerializer(serializers.ModelSerializer): #used generics for 
    class Meta: #should learn how 
        model = HouseList
        fields = ['id', 'location_city', 'developer', 'price', 'reserved', 'sold']
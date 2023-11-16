
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import HouseList
from .serializers import HouseSerializer





@api_view(['GET', 'POST'])
def house_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        houses = HouseList.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def house_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        house = HouseList.objects.get(pk=pk)
    except HouseList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

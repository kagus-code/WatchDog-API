from re import search
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response

from rest_framework import generics


# api imports 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  NeighbourHood
from .serializer import NeighbourhoodSerializer
from rest_framework import permissions, status
from rest_framework import filters


# Create your views here.

class NeighbourhoodApiView(APIView):
  serializer_class = NeighbourhoodSerializer

  def get(self, request, format=  None):
    all_hoods = NeighbourHood.objects.all()
    serializers = NeighbourhoodSerializer(all_hoods,many=True)
    return Response (serializers.data)

  def post(self,request):
    serializer =self.serializer_class(data=request.data)


    if serializer.is_valid(raise_exception=True):
      serializer.save()
      neighbourhood_data =serializer.data

      response={
        "data":{
            "neighbourhood":dict(neighbourhood_data),
            "status":"success",
            "message":"neighbourhood added successfully",
        }
      }


      return Response(response, status=status.HTTP_201_CREATED)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleHood(APIView):
  def get_hood(self,pk):
    try:
      return NeighbourHood.objects.get(pk=pk)
    except NeighbourHood.DoesNotExist:
      return Http404

  def get(self,request,pk,format=None):
    hood =self.get_hood(pk)
    serializers = NeighbourhoodSerializer(hood)
    return Response(serializers.data)    
  
  def put(self,request,pk,format=None):
    hood = self.get_hood(pk)
    serializers = NeighbourhoodSerializer(hood , request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
  
  def delete(self, request, pk, format=None):
    hood = self.get_hood(pk)
    hood.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  


class SearchHood(generics.ListCreateAPIView):
  search_fields =['name']
  filter_backends = (filters.SearchFilter,)
  queryset = NeighbourHood.objects.all()
  serializer_class = NeighbourhoodSerializer




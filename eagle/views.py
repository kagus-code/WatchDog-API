from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response

# api imports 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  NeighbourHood
from .serializer import NeighbourhoodSerializer
from rest_framework import permissions, status


# Create your views here.

class NeighbourhoodApiView(APIView):
  serializer_class = NeighbourhoodSerializer

  def post(self,request):
    serializer =self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
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


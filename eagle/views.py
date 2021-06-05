from re import search
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response

from rest_framework import generics


# api imports 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  NeighbourHood,Business,Post
from .serializer import NeighbourhoodSerializer,BusinessSerializer,PostSerializer
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





class BusinessApiView(APIView):
  serializer_class = BusinessSerializer
  def get(self, request, format=  None):
    all_businesss = Business.objects.all()
    serializers = BusinessSerializer(all_businesss,many=True)
    return Response (serializers.data)
  def post(self,request):
    serializer =self.serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      business_data =serializer.data
      response={
        "data":{
            "business":dict(business_data),
            "status":"success",
            "message":"business added successfully",
        }
      }
      return Response(response, status=status.HTTP_201_CREATED)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessSortAPIView(APIView):
  def get(self,request,hood):
    hood=self.kwargs.get('hood')
    business = Business.objects.filter(neighbourhood=hood)
    serializers= b=BusinessSerializer(business, many = True)
    return Response(serializers.data)

class SingleBusiness(APIView):
  def get_business(self,pk):
    try:
      return Business.objects.get(pk=pk)
    except Business.DoesNotExist:
      return Http404

  def get(self,request,pk,format=None):
    business =self.get_business(pk)
    serializers = BusinessSerializer(business)
    return Response(serializers.data)    
  
  def put(self,request,pk,format=None):
    business = self.get_business(pk)
    serializers = BusinessSerializer(business , request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
  
  def delete(self, request, pk, format=None):
    business = self.get_business(pk)
    business.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  
class SearchBusiness(generics.ListCreateAPIView):
  search_fields =['name']
  filter_backends = (filters.SearchFilter,)
  queryset = Business.objects.all()
  serializer_class = BusinessSerializer




class PostApiView(APIView):
  serializer_class = PostSerializer
  def get(self, request, format=  None):
    all_posts = Post.objects.all()
    serializers = PostSerializer(all_posts,many=True)
    return Response (serializers.data)
  def post(self,request):
    serializer =self.serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      business_data =serializer.data
      response={
        "data":{
            "business":dict(business_data),
            "status":"success",
            "message":"post added successfully",
        }
      }
      return Response(response, status=status.HTTP_201_CREATED)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SinglePost(APIView):
  def get_post(self,pk):
    try:
      return Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      return Http404

  def get(self,request,pk,format=None):
    post =self.get_post(pk)
    serializers = PostSerializer(post)
    return Response(serializers.data)    
  
  def put(self,request,pk,format=None):
    post = self.get_post(pk)
    serializers = PostSerializer(post , request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
  
  def delete(self, request, pk, format=None):
    post = self.get_post(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  
class SearchPost(generics.ListCreateAPIView):
  search_fields =['post']
  filter_backends = (filters.SearchFilter,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostSortAPIView(APIView):
  def get(self,request,hood):
    hood=self.kwargs.get('hood')
    post = Post.objects.filter(hood=hood)
    serializers= PostSerializer(post, many = True)
    return Response(serializers.data)
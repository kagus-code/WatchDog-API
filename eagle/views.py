from re import search
from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response

from rest_framework import generics


# api imports 
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  NeighbourHood,Business,Post,Profile,User
from .serializer import NeighbourhoodSerializer,BusinessSerializer,PostSerializer,ProfileSerializer,UserSerializer
from rest_framework import permissions, status
from rest_framework import filters

# authentication api view imports


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProfileAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

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
    serializers=BusinessSerializer(business, many = True)
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


class ProfileApiView(APIView):
  serializer_class = ProfileSerializer
  def get(self, request, format=  None):
    all_profiles = Profile.objects.all()
    serializers = ProfileSerializer(all_profiles,many=True)
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
            "message":"profile added successfully",
        }
      }
      return Response(response, status=status.HTTP_201_CREATED)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleProfile(APIView):
  def get_profile(self,pk):
    try:
      return Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
      return Http404

  def get(self,request,pk,format=None):
    profile =self.get_profile(pk)
    serializers = ProfileSerializer(profile)
    return Response(serializers.data)    
  
  def put(self,request,pk,format=None):
    profile = self.get_profile(pk)
    serializers = ProfileSerializer(profile , request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
  
  def delete(self, request, pk, format=None):
    profile = self.get_profile(pk)
    profile.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  



class UserApiView(APIView):
  serializer_class = UserSerializer
  def get(self, request, format=  None):
    all_users = User.objects.all()
    serializers = UserSerializer(all_users,many=True)
    return Response (serializers.data)
  def post(self,request):
    serializer =self.serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      user_data =serializer.data
      response={
        "data":{
            "user":dict(user_data),
            "status":"success",
            "message":"user added successfully",
        }
      }
      return Response(response, status=status.HTTP_201_CREATED)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSortAPIView(APIView):
  def get(self,request,hood):
    hood=self.kwargs.get('hood')
    user = User.objects.filter(neighbourhood=hood)
    serializers= b=UserSerializer(user, many = True)
    return Response(serializers.data)

class SingleUser(APIView):
  def get_user(self,pk):
    try:
      return User.objects.get(pk=pk)
    except User.DoesNotExist:
      return Http404

  def get(self,request,pk,format=None):
    user =self.get_user(pk)
    serializers = UserSerializer(user)
    return Response(serializers.data)    
  
  def put(self,request,pk,format=None):
    user = self.get_user(pk)
    serializers = UserSerializer(user , request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
  
  def delete(self, request, pk, format=None):
    user = self.get_user(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)  

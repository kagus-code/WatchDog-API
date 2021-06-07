from django.db.models import fields
from rest_framework import serializers
from .models import Business, NeighbourHood, Post, Profile, User


class NeighbourhoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = NeighbourHood
    fields = ('name','location','occupants_count')  

class BusinessSerializer(serializers.ModelSerializer):

  class Meta:
    model =Business
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

   class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

   def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

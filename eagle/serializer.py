from django.db.models import fields
from rest_framework import serializers
from .models import NeighbourHood


class NeighbourhoodSerializer(serializers.ModelSerializer):
  class Meta:
    model = NeighbourHood
    fields = ('name','location','occupants_count')  









  # def create(self, validated_data):
  #   hood = NeighbourHood.objects.create(validated_data)
  #   hood.save()
  #   return hood

  # def update(self,instance,validated_data):
  #   instance.name = validated_data.get('name',instance.name)
  #   instance.location = validated_data.get('location',instance.location)
  #   instance.occupants_count = validated_data.get('occupants_count',instance.occupants_count)
  #   instance.save()
  #   return instance



      # neighbourhood = NeighbourHood.objects.create(
      #   name =validated_data['name'],
      #   location = validated_data['location'],
      #   occupants_count = validated_data['occupants_count']
      # # )  
      # neighbourhood.save()
      # return neighbourhood

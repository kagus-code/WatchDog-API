from django.db import models
from django.contrib.auth.models import AbstractUser

class NeighbourHood(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  occupants_count=models.PositiveSmallIntegerField()


  def save_neighbourhood(self):
        self.save()


  @classmethod
  def delete_neighbourhood(cls,name):
    delete=NeighbourHood.objects.filter(name=name).delete()
    return delete

  @classmethod
  def find_neighbourhood(cls,id):
    neighbourhood = NeighbourHood.objects.filter(pk=id) 
    return neighbourhood
  @classmethod
  def update_neighbourhood(cls,name,new_name):
    update = NeighbourHood.objects.filter(name=name).update(name=new_name)
    return update 
  @classmethod
  def update_neighbourhood_occupants(cls,name,occupants):
    update_occupants = NeighbourHood.objects.filter(name=name).update(occupants_count=occupants)
    return update_occupants

  def __str__(self):
        return self.name

  class Meta:
        ordering = ['pk']   
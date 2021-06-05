from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db.models.fields import PositiveIntegerField


class NeighbourHood(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  occupants_count=models.PositiveSmallIntegerField()
  health_contact= PositiveIntegerField(null=True, blank=True)
  police_contact= PositiveIntegerField(null=True, blank=True)


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

  @classmethod
  def search_neighbourhood(cls,search_term):
    search = NeighbourHood.objects.filter(name__icontains= search_term)  
    return search

  def __str__(self):
        return self.name

  class Meta:
        ordering = ['pk']   

class User(AbstractUser):
   neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True,related_name='hood')


class Business(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='business_user')
  neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True,related_name='business_neighbourhood')
  email =models.EmailField()


  def __str__(self):
        return self.name

  class Meta:
        ordering = ['pk'] 



class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='post_hood')

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['-date']      


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user',null=True)
    profile_pic = CloudinaryField('image',null=True)
    bio = models.TextField(max_length=500,  blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='profile_hood')


    def save_profile(self):
        self.save()

    def delete_username(self, user_name):
        self.objects.filter(user_name=user_name).delete()

    @classmethod
    def update_username(cls,user_name,new_name):
        update = Profile.objects.filter(user_name=user_name).update(user_name=new_name)
        return update

    @classmethod
    def update_bio(cls,user_name,bio):
        update = Profile.objects.filter(user_name=user_name).update(bio=bio)
        return update

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['user'] 
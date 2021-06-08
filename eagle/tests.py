from django.test import TestCase
from .models import Profile,NeighbourHood,Business,Post

# Create your tests here.

class NeighbourhoodTestClass(TestCase):
  def setUp(self):
    self.neighbourhood = NeighbourHood(name='Kairu',location='Ruiru',occupants_count=50,health_contact=2221115,police_contact=2255562)
  def test_instance(self):
     self.assertTrue(isinstance(self.neighbourhood, NeighbourHood))

  def test_save_profile(self):
    self.neighbourhood.save_neighbourhood()
    hoods=NeighbourHood.objects.all()
    self.assertTrue(len(hoods) > 0)
  
  def test_update_neighbourhood_occupants(self):
      self.neighbourhood.save_neighbourhood()
      NeighbourHood.update_neighbourhood_occupants(name='kairu',occupants=30)
      self.assertTrue(NeighbourHood.objects.get(occupants_count=50))
  
  def test_update_neighbourhood_name(self):
    self.neighbourhood.save_neighbourhood()
    NeighbourHood.update_neighbourhood(name='Kairu',new_name='Kimbo')
    self.assertTrue(NeighbourHood.objects.get(name='Kimbo'))
    

  def tearDown(self):
        NeighbourHood.objects.all().delete() 

class ProfileTestClass(TestCase):
  def setUp(self):
     self.neighbourhood = NeighbourHood(name='Kairu',location='Ruiru',occupants_count=50,health_contact=2221115,police_contact=2255562)
     self.neighbourhood.save_neighbourhood()


     self.profile= Profile(user_name='king',profile_pic='clodinaryfield',bio='something personal',email='ekagus@gmail.com',phone_number='0701655877',hood=self.neighbourhood)
  
  def test_instance(self):
       self.assertTrue(isinstance(self.profile, Profile))

  def test_save_profile(self):
    self.profile.save_profile()
    profiles=Profile.objects.all()
    self.assertTrue(len(profiles) > 0)

  def test_delete_username(self):
    self.profile.save_profile()
    Profile.delete_username(Profile,user_name='king')
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) == 0)  

  def test_update_profile(self):
    self.profile.save_profile()
    Profile.update_bio(user_name='king',bio='new-bio')
    self.assertTrue(Profile.objects.get(bio='new-bio'))

  def tearDown(self):
        Profile.objects.all().delete() 
        NeighbourHood.objects.all().delete() 


class BusinessTestClass(TestCase):
  def setUp(self):
    self.neighbourhood = NeighbourHood(name='Kairu',location='Ruiru',occupants_count=50,health_contact=2221115,police_contact=2255562)
    self.neighbourhood.save_neighbourhood()

    self.business = Business(name='shopiz',description='selling',email="shopiz@gmail.com", neighbourhood=self.neighbourhood)
  def test_instance(self):
     self.assertTrue(isinstance(self.business, Business))

  def tearDown(self):
        Business.objects.all().delete() 
        NeighbourHood.objects.all().delete()    

class PostTestClass(TestCase):
  def setUp(self):
    self.neighbourhood = NeighbourHood(name='Kairu',location='Ruiru',occupants_count=50,health_contact=2221115,police_contact=2255562)
    self.neighbourhood.save_neighbourhood()

    self.post = Post(name='kagus',post='fire',date=2012-20-14, hood=self.neighbourhood)
  def test_instance(self):
     self.assertTrue(isinstance(self.post, Post))

  def tearDown(self):
        Post.objects.all().delete() 
        NeighbourHood.objects.all().delete()   
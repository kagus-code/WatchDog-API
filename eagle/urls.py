from django.urls import path, re_path


from . import views



urlpatterns = [

  re_path(r'hood-get/(?P<pk>[0-9]+)/$',views.SingleHood.as_view(),name="single-hood"),
  re_path(r'^hood-post/$', views.NeighbourhoodApiView.as_view(),name="post-hood"),


]

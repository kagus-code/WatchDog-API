from django.urls import path, re_path


from . import views



urlpatterns = [

  re_path(r'^hood-get/$', views.NeighbourhoodApiView.as_view(),name="get-hood"),
  re_path(r'^hood-post/$', views.NeighbourhoodApiView.as_view(),name="post-hood"),


]

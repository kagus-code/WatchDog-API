from django.urls import path, re_path


from . import views



urlpatterns = [
#neighbourhood urls
  re_path(r'hood-get/(?P<pk>[0-9]+)/$',views.SingleHood.as_view(),name="single-hood"),
  re_path(r'^hood-post/$', views.NeighbourhoodApiView.as_view(),name="post-hood"),
  re_path(r'^hood-search/', views.SearchHood.as_view(), name='search_hood'),
#business urls
  re_path(r'business-get/(?P<pk>[0-9]+)/$',views.SingleBusiness.as_view(),name="single-business"),
  re_path(r'^business-post/$', views.BusinessApiView.as_view(),name="post-business"),
  re_path(r'^business-search/', views.SearchBusiness.as_view(), name='search_business'),
  re_path(r'^business-hood/(?P<hood>\w+)/$', views.BusinessSortAPIView.as_view(), name='business_hood'),
#post urls
  
  re_path(r'post-get/(?P<pk>[0-9]+)/$',views.SinglePost.as_view(),name="single-post"),
  re_path(r'^post-post/$', views.PostApiView.as_view(),name="post-post"),
  re_path(r'^post-search/', views.SearchPost.as_view(), name='search_post'),
  re_path(r'^post-hood/(?P<hood>\w+)/$', views.PostSortAPIView.as_view(), name='post_hood'),


]

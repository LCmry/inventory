from django.conf.urls import url
from inventory_app import views

urlpatterns = [url(r'^$', views.index, name='index'),
              url(r'^categories/', views.categories, name='categories'),
              url(r'^outlets/', views.outlets, name='outlets'),
              url(r'^item/(?P<id>[0-9]+)/$', views.item, name='item'),
              url(r'^category/(?P<id>[0-9]+)/$', views.category, name='category'),
              url(r'^outlet/(?P<id>[0-9]+)/$', views.outlet, name='outlet'),
              ]
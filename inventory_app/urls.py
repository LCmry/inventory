from django.conf.urls import url
from inventory_app import views

urlpatterns = [url(r'^$', views.index, name='index'),
              ]
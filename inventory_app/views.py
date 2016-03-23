from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse

from inventory_app.models import Item, Category, Outlet

def index(request):
  items = Item.objects.all()
  t = loader.get_template('index.html')
  c = Context({ 'items': items, })
  return HttpResponse(t.render(c))

def categories(request):
  categories = Category.objects.all().order_by('-name')
  t = loader.get_template('catgories.html')
  c = Context({ 'categories': categories, })
  return HttpResponse(t.render(c))

def outlets(request):
  outlets = Outlet.objects.all().order_by('-name')
  t = loader.get_template('outlets.html')
  c = Context({ 'outlets': outlets, })
  return HttpResponse(t.render(c))

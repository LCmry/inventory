from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.http import HttpResponse

from inventory_app.models import Item, Category, Outlet, Count

def index(request):
  items = Item.objects.all()
  t = loader.get_template('index.html')
  c = Context({ 'items': items, })
  return HttpResponse(t.render(c))

def categories(request):
  categories = Category.objects.all().order_by('name')
  t = loader.get_template('categories.html')
  c = Context({ 'categories': categories, })
  return HttpResponse(t.render(c))

def outlets(request):
  outlets = Outlet.objects.all().order_by('name')
  t = loader.get_template('outlets.html')
  c = Context({ 'outlets': outlets, })
  return HttpResponse(t.render(c))

def category(request, id):
  category = get_object_or_404(Category, id=id)
  items = Item.objects.filter(category=id)
  t = loader.get_template('category.html')
  c = Context({ 'category': category, 'items': items })
  return HttpResponse(t.render(c))

def outlet(request, id):
  outlet = get_object_or_404(Outlet, id=id)
  counts = Count.objects.filter(outlet=id)
  items = [c.item for c in counts]
  t = loader.get_template('outlet.html')
  c = Context({ 'outlet': outlet, 'items': items })
  return HttpResponse(t.render(c))

def item(request, id):
  item = get_object_or_404(Item, id=id)
  t = loader.get_template('item.html')
  c = Context({ 'item': item })
  return HttpResponse(t.render(c))

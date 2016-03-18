from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse

from inventory_app.models import Item

def index(request):
  items = Item.objects.all()
  t = loader.get_template('inventory_app/index.html')
  c = Context({ 'items': items, })
  return HttpResponse(t.render(c))

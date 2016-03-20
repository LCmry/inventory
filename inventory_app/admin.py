from django.contrib import admin
from inventory_app.models import Item, Category, Outlet

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Outlet)

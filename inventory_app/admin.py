from django.contrib import admin
from inventory_app.models import Item, Category, Outlet, Count

admin.site.register(Category)
admin.site.register(Outlet)

class CountInline(admin.TabularInline):
  model = Count

class ItemAdmin(admin.ModelAdmin):
  inlines = (CountInline,)

admin.site.register(Item, ItemAdmin)
from django.contrib import admin
from .models import State, Property

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'state', 'acre_price', 'acre', 'available', 'road_width')  
    list_filter = ('state', 'available')  
    search_fields = ('property_name', 'state__name')  

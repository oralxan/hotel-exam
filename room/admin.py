from django.contrib.admin import *
from .models import Room
@register(Room)
class RoomAdmin(ModelAdmin):
    list_display = ('id','description')
    list_display_links = ('id','description')
    ordering = ('id',)
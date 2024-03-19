from django.contrib.admin import *
from .models import Guest
@register(Guest)
class RoomAdmin(ModelAdmin):
    list_display = ('id','first_name')
    list_display_links = ('id','first_name')
    ordering = ('id',)
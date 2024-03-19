from django.contrib.admin import *
from .models import Booking
@register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ('id','rooms')
    list_display_links = ('id','rooms')
    ordering = ('id',)
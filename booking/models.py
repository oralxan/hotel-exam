from django.db.models import *
from room.models import Room
from guest.models import Guest


class Booking(Model):
    rooms =OneToOneField(
        Room,
        verbose_name='room',
        on_delete=CASCADE

    )
    author = ForeignKey(
        Guest,
        verbose_name='guest',
        on_delete=CASCADE
        
    )
    chack_in_date = DateField(
        'In date',
        auto_now=True
    )
    chack_on_date = DateField(
        'ON DATE'
    )
    is_paid = BooleanField(
        'Paid id',
        default=False
      
        
    )
    def __str__(self):
        return f'{self.author}'

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

from django.db.models import *
from hotel.models import Hotel

class Room(Model):
    hotel=OneToOneField(
        Hotel,
        verbose_name='hatel',
        on_delete=CASCADE

    )
    number = IntegerField(
        'number',
        default=1

    )
    capacity = IntegerField(
        'capacity',
        default=1
    )
    price_per_night=IntegerField(
        'price_per_night'
        
    )
    is_used=BooleanField(
        'Is used',
        default=False
    )
    description=TextField(
        'about room',
        blank=True,
        null=True
    )
    image= ImageField(
        'image of room',
        upload_to='rooms-img/%Y/%m/%d'
    )
    def __str__(self) :
        return f'{self.id}'
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
    




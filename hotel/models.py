from django.db.models import *

class Hotel(Model):
    name = CharField(
        'Host name',
        max_length=256
    )
    address=CharField(
        'address of  the host',
        blank=True,
        null=True,
        max_length=250
    )
    city=CharField(
        'city',
        max_length=50
    )
    country=CharField(
        'country',
        max_length=50

    )
    rating = PositiveIntegerField(
        'rating',
        default=0
        
    )
    image = ImageField(
        'Img',
        upload_to='hotels-img/%Y/%m/%d'
    )
    description = TextField(
        'Description',
        blank=True,
        null= True
    )
    def __str__(self) :
        return f'{self.name}'
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'
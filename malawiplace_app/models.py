from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Airline(models.Model):
    airline_name = models.CharField(max_length=200, null=True)
    airline_logo = models.ImageField(blank=True, upload_to='airline_logo/')

    def __str__(self):
        return self.airline_name


class Flight(models.Model):
    Depatures = (
        ('lilongwe', 'lilongwe'),
        ('Blantyre', 'Blantyre'),
        ('Mzuzu', 'Mzuzu'),
    )
    Destinations = (
        ('Paris', 'Paris'),
        ('New York', 'New York'),
        ('London ', 'London'),
    )
    Class = (
        ('First Class', 'First Class'),
        ('Economy', 'Economy'),
        ('Standard', 'Standard'),
    )
    airline = models.ForeignKey(Airline, null=False, on_delete=models.CASCADE)
    flight_name = models.CharField(max_length=200, null=True)
    Final_destination = models.CharField(choices=Destinations, max_length=200, null=True)
    depature_place = models.CharField(choices=Depatures ,max_length=200, null=True)
    depature_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    return_ticket = models.BooleanField(default=False)
    capacity = models.IntegerField(default=1)
    cabin_class = models.CharField(choices=Class, max_length=100, null=True)
    price = models.FloatField(null=True, default=0)

    def __str__(self):
        return '{} {}'.format(self.airline.airline_name, self.flight_name)


class BookFlight(models.Model):
    pass


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255, null=True)
    rooms = models.IntegerField(default=1, null=True)
    slug = models.SlugField(max_length=255)

    # def get_absolute_url(self):
    #     return reverse('hotel-list', args=[self.slug])

    def __str__(self):
        return self.hotel_name


class RoomManager(models.Manager):
    def get_queryset(self):
        return super(RoomManager, self).get_queryset().filter(is_booked=True)


class Room(models.Model):
    ROOM_CAT = (
        ('Deluxe', 'Deluxe'),
        ('Standard', 'Standard'),
        ('Executive', 'Executive'),
        ('Presidential', 'Presidential'),
    )

    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE, null=False)
    location = models.CharField(max_length=300, null=False)
    description = models.TextField()
    price = models.CharField(max_length=100, null=False)
    room_category = models.CharField(max_length=400, choices=ROOM_CAT)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    num_of_beds = models.IntegerField(default=1, null=True)
    is_booked = models.BooleanField(default=False)
    room = RoomManager() 
    objects = models.Manager()

    def __str__(self):
        return '{}  {} '.format(self.hotel.hotel_name, self.room_category)


class BookRoom(models.Model):
    customer_name = models.CharField(max_length=255, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False)
    # room_type = models.CharField(max_length=255, choices=ROOM_CAT)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    # num_of_beds = models.IntegerField(default=1, null=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=255, default='+265', null=True)
    additional_reservations = models.TextField(blank=True)
    number_of_rooms = models.IntegerField(default=1, blank=False)

    def __str__(self):
        return ' booking for {} at {} '.format(self.customer_name, self.room.hotel.hotel_name)


class CarRental(models.Model):
    rental_name= models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.rental_name


class Car(models.Model):
    CAR_TYPES = (
        ('Executive', 'Executive'),
        ('Standard', 'Standard'),
        ('Small', 'Small'),
    )
    Destinations = (
        ('lilongwe', 'lilongwe'),
        ('Blantyre', 'Blantyre'),
        ('Mzuzu', 'Mzuzu'),
    )
    
    car_rental = models.ForeignKey(CarRental,on_delete=models.CASCADE, null=False)
    car_type = models.CharField(choices=CAR_TYPES, null=True, max_length=100)
    car_name = models.CharField(max_length=200, null=True)
    pick_up = models.DateTimeField(blank=True, null=True)
    Drop_off = models.DateTimeField(blank=True, null=True)
    passengers = models.IntegerField(default=1)
    destination = models.CharField(choices=Destinations, max_length=300, null=True)
    pick_up_location = models.CharField(choices=Destinations, max_length=300, null=True)
    bus = models.BooleanField(default=False)
    price = models.FloatField(null=True, default=0)

    def __str__(self):
        return '{}\'s {}'.format(self.car_rental.rental_name, self.car_name)


class RentCar(models.Model):
    pass


class Blog(models.Model):
    CATEGORY = (
        ('Travel', 'Travel'),
        ('Cars', 'Cars'),
        ('Nature', 'Nature'),
    )

    title = models.CharField(max_length=200, null=True)
    content = models.TextField(blank=False)
    content_2 = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='blog_img', blank=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.title


class About(models.Model):
    company_name = models.CharField(null=True, max_length=300)
    content = models.TextField(null=True)
    content_2 = models.TextField(null=True)
    extra_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class ContactDetail(models.Model):
    company_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True)   
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    open_days = models.CharField(max_length=50, null=True)
    open_time = models.CharField(max_length=50, null=True)

    def __str__(self):
        return 'Contacts(Don\'t add multiple just edit)'


class Logo(models.Model):
    logo_name = models.CharField(max_length=200, null=True)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.logo_name


class PlaceCountry(models.Model):
    continent_or_country = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.continent_or_country


class Place(models.Model):
    place_country = models.ForeignKey(PlaceCountry, on_delete=models.CASCADE, null=True)
    place_name= models.CharField(max_length=200, null=True)
    about_place = models.TextField(null=True)
    extra_content = models.TextField(null=True)
    img = models.ImageField(blank=False, upload_to='places/')

    def __str__(self):
        return self.place_name


class Testimonial(models.Model):
    name = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=100, null=True)
    content = models.TextField(max_length=300, null=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    img = models.ImageField(blank=True, upload_to='event_img/')
    event_name = models.CharField(max_length=200, null=True)
    event_description = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=300, null=False)

    def __str__(self):
        return self.event_name


class BookEvent(models.Model):
    name_of_event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    customer_name = models.CharField(max_length=255, null=True)  
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=255, default='+265', null=True)
    number_of_tickets = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'Event Booking for {} at the {}'.format(self.customer_name, self.name_of_event.event_name)  


class Restrant(models.Model):
    restrant_name = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=200, null=True)
    logo = models.ImageField(blank=False, upload_to='restrant_img/')

    def __str__(self):
        return self.restrant_name


class BusCompany(models.Model):
    company_name = models.CharField(max_length=255, null=True)
    buses = models.IntegerField(default=1, null=True)
    slug = models.SlugField(max_length=255)
    bus_logo = models.ImageField(upload_to='bus_company_img')

    class Meta:
        verbose_name_plural = 'Bus Companies'

    def __str__(self):
        return self.company_name


class Bus(models.Model):
    bus_company = models.ForeignKey(BusCompany, on_delete=models.CASCADE, null=True)
    bus_name = models.CharField(max_length=255, null=True)
    depature_point = models.CharField(max_length=255, null=True)
    destination_point = models.CharField(max_length=255, null=True)
    price = models.FloatField(default=0.00)
    depature_time = models.TimeField(null=True)
    description = models.TextField(blank=True, null=True)
    max_capacity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Buses'

    def __str__(self):
        return '{} from {}'.format(self.bus_name, self.bus_company.company_name)

    
class BookBus(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, null=True)
    passenger_name = models.CharField(max_length=255, null=True)
    number_of_seats = models.IntegerField(default=1)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=255, default='+265', null=True)
    date = models.DateField(null=True)

    class Meta:
        verbose_name_plural = 'Book Buses'

    def __str__(self):
        return 'booking for {} , {}'.format(self.passenger_name, self.bus.bus_company)

from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'rooms','slug']
    prepopulated_fields = {'slug': ('hotel_name',)}

@admin.register(BusCompany)
class BusAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'buses','slug']
    prepopulated_fields = {'slug': ('company_name',)}

admin.site.register(Bus)
admin.site.register(BookBus)
admin.site.register(BookRoom)
admin.site.register(Flight)
admin.site.register(Airline)
# admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(CarRental)
admin.site.register(Car)
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Logo)
admin.site.register(ContactDetail)
admin.site.register(Testimonial)
admin.site.register(Place)
admin.site.register(PlaceCountry)
admin.site.register(Restrant)
admin.site.register(Event)

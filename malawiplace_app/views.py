from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .filters import Flightfilter
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .forms import RoomBookingForm, BusBookingForm, EventBookingForm
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import datetime
# Create your views here.

def home(request):
    flights = Flight.objects.all()
    airlines = Airline.objects.all()
    event_items = Event.objects.all()
    country_places = PlaceCountry.objects.all()
    places = Place.objects.all()

    context = {
        'flights': flights,
        'airlines': airlines,
        'events': event_items,
        'country_places': country_places,
        'places': places,
    }
    return render(request,'malawiplace_app/index.html', context)


def flight_search_view(request):
    if request.method == 'POST':

        #get data from template
        depature_place = request.POST['depature_place']
        destination = request.POST['destination']
        depature_date = request.POST['depature_date']
        return_date = request.POST['return_date']
        num_of_adults = request.POST['capacity']
        cabin_class = request.POST.get('cabin_class', False)

        #check matching fields

        
        return_date = datetime.strptime(return_date, '%Y-%m-%d')
        depature_date = datetime.strptime(depature_date, '%Y-%m-%d')
        print(return_date)
        print(depature_date)
        
        result = Flight.objects.filter(Q(depature_place__icontains=depature_place)&Q(Final_destination__icontains=destination)&Q(cabin_class__icontains=cabin_class)&Q(return_date__gte=datetime.date(return_date))&Q(depature_date__lte=datetime.date(depature_date)))
        

        #render the data
        context = {
            'searched': destination,
            'flight_search': result,
            }
        
        return render(request, 'malawiplace_app/tickets.html', context)
    else:
        context = {

        }
        return render(request, 'malawiplace_app/tickets.html')


def hotel_search_view(request):
    if request.method == 'POST':

        #get data from template
        location = request.POST['location']
        # arrival = request.POST['arrival']
        # return_date = request.POST['return']
        num_of_rooms = request.POST['rooms']
        num_of_beds = request.POST['capacity']
        room_category = request.POST['category']

        
        if num_of_beds == '':
            return messages.error(request, 'Document deleted.')

        result = Room.room.filter(Q(location__icontains=location)&Q(room_category__icontains=room_category)&Q(num_of_beds__gte=num_of_beds)) 

        #render the data
        context = {
            'searched': location,
            'hotel_search': result,
            }
  
        return render(request, 'malawiplace_app/hotels.html', context)
    else:
        context = {

        }
        return render(request, 'malawiplace_app/hotels.html')



def car_search_view(request):
    if request.method == 'POST':

        #get data from template
        car = request.POST['car_name']
        destination = request.POST['destination']
        category = request.POST['category']
        num_passengers = request.POST['passengers']
        # num_of_adults = request.POST['capacity']
        #precision filter
    
        result = Car.objects.filter(Q(car_name__icontains=car)&Q(destination__icontains=destination)&Q(car_type__icontains=category)&Q(passengers__gte=num_passengers))
        
        #render the data
        context = {
            'searched': destination,
            'car_search': result,
            }
            
        return render(request, 'malawiplace_app/cars.html', context)
    else:
        context = {

        }
        return render(request, 'malawiplace_app/cars.html')


def about(request):
    about_details = About.objects.all()
    testimonials = Testimonial.objects.all

    context = {
        'about': about_details, 
        'testimonial': testimonials,
    }
    return render(request, 'malawiplace_app/overview.html', context)

def blog_view(request):
    blogs = Blog.objects.all().order_by('-date')
    page = Paginator(blogs, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
    }
    return render(request, 'malawiplace_app/blog-masonry.html', context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'malawiplace_app/blog-single-post.html'


def events(request):
    event_items = Event.objects.all()
    page = Paginator(event_items, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
    }
    return render(request, 'malawiplace_app/events.html', context)


class EventDetailView(DetailView):
    model = Event
    template_name = 'malawiplace_app/event_detail.html'


class EventBookingView(CreateView):
    model = BookBus
    form_class = EventBookingForm
    success_url = reverse_lazy('success')
    template_name = 'malawiplace_app/event-booking-form.html'
    success_message = "your booking was successfully processed"

    def form_valid(self, form):
        form.instance.event_id = self.kwargs['pk']
        return super().form_valid(form)


def event_search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        events = Event.objects.filter(event_name__icontains=searched)
        context = {
            'searched': searched,
            'events': events,
        }
        return render(request, 'malawiplace_app/event_searched.html', context)
    else:
        context = {

        }
        return render(request, 'malawiplace_app/event_searched.html')


def restrant_view(request):
    restrants = Restrant.objects.all()
    page = Paginator(restrants, 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
    }
    return render(request, 'malawiplace_app/restrants.html', context)


def contact(request):

    contact_details = ContactDetail.objects.all()
    
    context = {
        'contact': contact_details
    }

    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        data = {
            'name': name,
            'email': email,
            'message': message,
            'phone': phone,
            'surname': surname,
        }
        message = '''
        email : {}
        New message: {}
        From: {} {}
        Phone number: {}
        From malawi place website.
        '''.format(data['email'], data['message'], data['name'], data['surname'], data['phone'])
        send_mail(email, message, '', ['wonganitemborgb2@gmail.com'])
        # print(data)
        return render(request, 'malawiplace_app/contacts.html', {'name':name, 'details':contact_details})
    else:
        return render(request, 'malawiplace_app/contacts.html', {'details': contact_details})


def restaurant_search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        restaurants = Restrant.objects.filter(restrant_name__icontains=searched)
        context = {
            'searched': searched,
            'restrant': restaurants,
        }
        return render(request, 'malawiplace_app/restaurant_search.html', context)
    else:
        context = {

        }
        return render(request, 'malawiplace_app/restaurant_search.html')


def blog_search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        blog = Blog.objects.filter(title__icontains=searched)
        context = {
            'searched': searched,
            'blog': blog,
        }
        return render(request, 'malawiplace_app/blog_search.html', context)
    else:
        context = {

        }
        return render(request, 'malawiplace_app/blog_search.html')


def success(request):
    return render(request, 'malawiplace_app/success.html')


def hotel_room_booking(request, pk):
    room = get_object_or_404(Room, pk=pk)
           
    context = {
        'room': room,
        
    }
    return render(request, 'malawiplace_app/room-detail.html', context)


class RoomBookingView(CreateView):
    model = BookRoom
    form_class = RoomBookingForm
    success_url = reverse_lazy('success')
    template_name = 'malawiplace_app/forms.html'
    success_message = "your booking was successfully processed"

    def form_valid(self, form):
        form.instance.room_id = self.kwargs['pk']

        return super().form_valid(form)


def bus_list(request):

    get_buses = Bus.objects.all()
    page = Paginator(get_buses, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'page': page,
    }
    return render(request, 'malawiplace_app/bus-list.html', context)

def bus_search_view(request):
    if request.method == 'POST':
        depature = request.POST['departure']
        destination = request.POST['destination']
        print (depature, destination)

        buses = Bus.objects.filter(
            depature_point__icontains=depature
        ).filter(
            destination_point__icontains=destination
        )

        context = {
            'searched': destination,
            'bus': buses,
        }
        return render(request, 'malawiplace_app/bus-search-list.html', context)
    else:
        context = {

        }
        return render(request, 'malawiplace_app/bus-search-list.html')



def bus_details(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
           
    context = {
        'bus': bus,
        
    }
    return render(request, 'malawiplace_app/bus-detail.html', context)


class BusBookingView(CreateView):
    model = BookBus
    form_class = BusBookingForm
    success_url = reverse_lazy('success')
    template_name = 'malawiplace_app/bus-form.html'
    success_message = "your booking was successfully processed"

    def form_valid(self, form):
        form.instance.bus_id = self.kwargs['pk']
        return super().form_valid(form)

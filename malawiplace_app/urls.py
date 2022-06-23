from django.urls import path
from django.contrib import admin
from . import views

# app_name = "malawiplace_app"

urlpatterns = [
    path('',views.home, name='Home'),
    path('flight_search/',views.flight_search_view, name='flight_search'),
    path('hotel_search/',views.hotel_search_view, name='hotel_search'),
    path('car_search/',views.car_search_view, name='car_search'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_view, name='blog'),
    path('blog_single/<pk>/', views.BlogDetailView.as_view(), name='blog_single'),
    path('restrant/', views.restrant_view, name='restrants'),
    path('event_single/<pk>/', views.EventDetailView.as_view(), name='event_single'),
    path('event_single/<pk>/book/', views.EventBookingView.as_view(), name='event-booking'),
    path('event/', views.events, name='events'),
    path('event_searched/', views.event_search_view, name='event_search'),
    path('restaurant_searched/', views.restaurant_search_view, name='restaurant_search'),
    path('blog_searched/', views.blog_search_view, name='blog_search'),
    path('about/', views.about, name='about'),
    path('success/', views.success, name='success'),
    path('room_details/<int:pk>/', views.hotel_room_booking, name='room-details'),
    path('room_details/<int:pk>/book/', views.RoomBookingView.as_view(), name='room-details-book'),
    path('bus_list/', views.bus_list, name='bus-list'),
    path('bus_details/<int:pk>/',views.bus_details, name='bus-details'),
    path('bus_details/<int:pk>/bus_book/', views.BusBookingView.as_view(), name='bus-book'),
    path('bus_search/', views.bus_search_view, name='bus-search'),
]


admin.site.site_header = "Malawi Place Admin"
admin.site.site_title = "Malawi Place"
admin.site.index_title = "Malawi Place"
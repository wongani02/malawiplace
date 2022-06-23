from django import forms
from .models import BookRoom, BookBus, BookEvent
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from django.forms import ModelForm


class RoomBookingForm(ModelForm):

    customer_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholders': 'full name'}
        ),
        required=True
    )

    phone_number =  forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

    number_of_rooms = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )

    additional_reservations = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )

    check_in = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control'}
        ),
        required = True
    )

    check_out = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control'}
        ),
        required = True
    )


    class Meta:
         model = BookRoom
         fields = ['customer_name' , 'check_in', 'check_out', 'email', 'phone_number', 'additional_reservations', 'number_of_rooms']


class BusBookingForm(ModelForm):

    passenger_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholders': 'full name'}
        ),
        required=True
    )

    phone_number =  forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

    date = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={'class': 'form-control'}
        ),
        required = True
    )

    number_of_seats = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = BookBus
        fields = ['passenger_name', 'email', 'phone_number', 'date', 'number_of_seats']


class EventBookingForm(forms.ModelForm):

    customer_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholders': 'full name'}
        ),
        required=True
    )

    phone_number =  forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

    number_of_tickets = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = BookEvent
        fields = ['customer_name', 'phone_number', 'email', 'number_of_tickets']

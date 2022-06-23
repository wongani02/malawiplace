import django_filters
from django_filters import NumberFilter, CharFilter
from .models import *
# from django.db import models

class Flightfilter(django_filters.FilterSet):
    flight_name = CharFilter(field_name='flight_name', lookup_expr='icontains')

    class meta:
        model = Flight
        fields = ['flight_name', 'depature_place', 'depature_date']
        # filter_overrides = {
        #      models.CharField: {
        #          'filter_class': django_filters.CharFilter,
        #          'extra': lambda f: {
        #              'lookup_expr': 'icontains',
        #          },
        #      },
        #     #  models.BooleanField: {
        #     #      'filter_class': django_filters.DateFilter,
        #     #      'extra': lambda f: {
        #     #          'widget': forms.CheckboxInput,
        #     #      },
        #     #  },
        #  }
import django_filters
from django_filters import rest_framework as filters
from .models import *
from django_filters import ModelChoiceFilter


class UserFilter(django_filters.FilterSet):

    brand = ModelChoiceFilter(
        field_name='brand',
        lookup_expr='isnull',
        queryset=Cars.objects.order_by('brand').values_list('brand').distinct(),
        method='filter_brand',
    )

    class Meta:
        model = Cars
        fields = {
            'brand': ['icontains'],
            'model': ['icontains'],
            'year': ['iexact', 'lte', 'gte'],
            'color': ['icontains'],
            'city': ['icontains'],
            'country': ['icontains'],
            'currency': ['icontains'],
            'price': ['lte', 'gte']
        }
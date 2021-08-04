from rest_framework import generics

from habi import paginators
from property.filters import PropertyFilter
from property.models import Property
from property.serializers.property_serializers import PropertySerializer

from django_filters import rest_framework as filters


class PropertyListView(generics.ListAPIView):
    serializer_class = PropertySerializer
    pagination_class = paginators.Paginator
    queryset = Property.objects.all().using("data")
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PropertyFilter

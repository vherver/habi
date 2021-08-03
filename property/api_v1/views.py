from rest_framework import generics

from habi import paginators
from property.models import Property
from property.serializers.property_serializers import PropertySerializer


class PropertyListView(generics.ListAPIView):
    serializer_class = PropertySerializer
    pagination_class = paginators.Paginator
    queryset = Property.objects.all()

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.

        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

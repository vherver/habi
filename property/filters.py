from django_filters import FilterSet, rest_framework

from property.models import Property


class PropertyFilter(FilterSet):
    min_price = rest_framework.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name="price", lookup_expr='lte')
    min_year = rest_framework.NumberFilter(field_name="year", lookup_expr='gte')
    max_year = rest_framework.NumberFilter(field_name="year", lookup_expr='lte')

    class Meta:
        model = Property
        fields = ["city", "price", "year"]

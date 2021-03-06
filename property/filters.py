from django_filters import CharFilter, FilterSet, rest_framework as filter

from property.models import Property


class PropertyFilter(FilterSet):
    min_price = filter.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filter.NumberFilter(field_name="price", lookup_expr="lte")
    min_year = filter.NumberFilter(field_name="year", lookup_expr="gte")
    max_year = filter.NumberFilter(field_name="year", lookup_expr="lte")
    status = CharFilter(method="filter_by_status", label="Status")

    class Meta:
        model = Property
        fields = ["city", "price", "year"]

    def filter_by_status(self, queryset, name, value):
        return queryset.filter(
            id__in=[
                property.id
                for property in queryset
                if property.get_status_name == value
            ]
        )

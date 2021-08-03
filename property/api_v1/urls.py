from django.urls import path

from property.api_v1.views import PropertyListView

urlpatterns = [
    path(
        "",
        PropertyListView.as_view(),
        name="property-list",
    ),
]

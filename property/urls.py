from django.urls import path

from property.views import Property

urlpatterns = [
    path(
        "", Property.as_view(), name="property",
    ),
]
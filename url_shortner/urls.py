from django.urls import path
from .views import short_url_view

urlpatterns = [
    path("", short_url_view, name="shorturl"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("quotation-details/", views.testing, name="quotation-details"),
]
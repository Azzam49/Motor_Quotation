from django.urls import path
from . import views
from .features.quotation import views as quotation_views
from .system import views as system_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("testing/", views.testing, name="testing"),
    path("quotation-form/", quotation_views.create_quotation, name="quotation-form"),
    path("quotation-submitted/", quotation_views.submit_quotation, name="quotation-submitted"),
    path("login/", system_views.login_view, name="login"),
    path("logout/", system_views.logout_view, name="logout"),
    path("quotation-details/", quotation_views.quotation_details, name="quotation-details"),

    path("send-emails/", system_views.send_emails, name="send-emails"),
]
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.models import User

from app.system.models import CustomerProfile
from .models import Quotation
from app.features.coverage_setting.models import CoverageSetting
from app.features.vehicle.models import Vehicle

from app.features.vehicle.forms import VehicleForm

from app.Common import common
from motor_quotation.tasks import send_email


def create_quotation(request):
    if request.user.is_authenticated:
        return redirect('quotation-details')

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        vehicle_model = request.POST.get("model")
        vehicle_price = request.POST.get("price")
        vehicle_year_make = request.POST.get("year_make")
        vehicle_number = request.POST.get("number")
        windscreen_coverage = True if request.POST.get("windscreen_coverage") == "yes" else False
        passenger_liability_coverage = True if request.POST.get("passenger_liability_coverage") == "yes" else False
        flood_coverage = True if request.POST.get("flood_coverage") == "yes" else False
        windstorm_coverage = True if request.POST.get("windstorm_coverage") == "yes" else False
        landslide_coverage = True if request.POST.get("landslide_coverage") == "yes" else False
        subsidence_coverage = True if request.POST.get("landslide_coverage") == "yes" else False
        quotation_price = request.POST.get("quotation_price")
        has_email_quotation_pdf = True if request.POST.get("email_quotation") == "on" else False

        # Create user's Django model
        user = User.objects.create(
            username= username,
            email= email,
        )
        generated_password = common.generate_password()
        user.set_password(generated_password)
        user.save()

        vehicle = Vehicle.objects.create(
            model = vehicle_model,
            number = vehicle_number,
            year_make = vehicle_year_make,
            price = vehicle_price,
        )
        vehicle.save()

        quotation = Quotation.objects.create(
            name= user.username+"_quotation",
            price= quotation_price,
            vehicle = vehicle,
            windscreen_coverage = windscreen_coverage,
            passenger_liability_coverage = passenger_liability_coverage,
            flood_coverage = flood_coverage,
            windstorm_coverage = windstorm_coverage,
            landslide_coverage = landslide_coverage,
            subsidence_coverage = subsidence_coverage,
        )

        customer_profile = CustomerProfile.objects.create(
            user= user,
            mobile= mobile,
            quotation = quotation
        )
        customer_profile.save()

        request.session['username-submit'] = username

        pdf_data = {
            'username': user.username,
            'email': user.email,
            'mobile': user.customerprofile.mobile,

            'vehicle_model': user.customerprofile.quotation.vehicle.model,
            'vehicle_price': user.customerprofile.quotation.vehicle.price,
            'vehicle_year': user.customerprofile.quotation.vehicle.year_make,
            'vehicle_number': user.customerprofile.quotation.vehicle.number,

            'quotation_price': user.customerprofile.quotation.price,

            'windscreen_coverage': 'Yes' if user.customerprofile.quotation.windscreen_coverage else 'No',
            'passenger_liability_coverage': 'Yes' if user.customerprofile.quotation.passenger_liability_coverage else 'No',
            'flood_coverage': 'Yes' if user.customerprofile.quotation.flood_coverage else 'No',
            'windstorm_coverage': 'Yes' if user.customerprofile.quotation.windstorm_coverage else 'No',
            'landslide_coverage': 'Yes' if user.customerprofile.quotation.landslide_coverage else 'No',
            'subsidence_coverage': 'Yes' if user.customerprofile.quotation.subsidence_coverage else 'No',
        }

        send_email.delay(
            title= 'Quotation Submitted Successfully',
            emails_list= [email],
            email_template= 'emails/email-success.html',
            text_alternative_email= 'emails/email-success.txt',
            email_context= {
                'username': username,
                'password': generated_password,
                'quotation_page_url': f"http://{get_current_site(request)}/quotation-details/"#,
            },
            pdf_data= pdf_data,
            pdf_template= 'emails/email-quotation-details.html',
            has_pdf= has_email_quotation_pdf
        )

        return redirect('quotation-submitted')
    else:
        context = {
            'VehicleForm': VehicleForm(),
            'formula_percentage': CoverageSetting.objects.get(name__exact='formula_percentage'),
            'subsidence_coverage': CoverageSetting.objects.get(name__exact='subsidence_coverage'),
            'landslide_coverage': CoverageSetting.objects.get(name__exact='landslide_coverage'),
            'windstorm_coverage': CoverageSetting.objects.get(name__exact='windstorm_coverage'),
            'flood_coverage': CoverageSetting.objects.get(name__exact='flood_coverage'),
            'passenger_liability_coverage': CoverageSetting.objects.get(name__exact='passenger_liability_coverage'),
            'windscreen_coverage': CoverageSetting.objects.get(name__exact='windscreen_coverage'),
            'title': 'Form'
        }
        return render(request, 'quotation.html', context)


def submit_quotation(request):
    context = {
            'username': request.session.get('username-submit'),
            'title': 'Successfull Submit'
        }
    return render(request, 'success.html', context)


@login_required(login_url = 'login')
def quotation_details(request):
    user = request.user

    try:
        context = {
            'username': user.username,
            'email': user.email,
            'mobile': user.customerprofile.mobile,

            'vehicle_model': user.customerprofile.quotation.vehicle.model,
            'vehicle_price': user.customerprofile.quotation.vehicle.price,
            'vehicle_year': user.customerprofile.quotation.vehicle.year_make,
            'vehicle_number': user.customerprofile.quotation.vehicle.number,

            'quotation_price': user.customerprofile.quotation.price,

            'windscreen_coverage': 'Yes' if user.customerprofile.quotation.windscreen_coverage else 'No',
            'passenger_liability_coverage': 'Yes' if user.customerprofile.quotation.passenger_liability_coverage else 'No',
            'flood_coverage': 'Yes' if user.customerprofile.quotation.flood_coverage else 'No',
            'windstorm_coverage': 'Yes' if user.customerprofile.quotation.windstorm_coverage else 'No',
            'landslide_coverage': 'Yes' if user.customerprofile.quotation.landslide_coverage else 'No',
            'subsidence_coverage': 'Yes' if user.customerprofile.quotation.subsidence_coverage else 'No',

            'title': 'Details'
        }
    except Exception as e:
        messages.error(request, f'There was error to load data, probably user {user.username} don\'t have quotation.')
        context = {
            'username': user.username,
            'email': user.email,
            'title': 'Details'
        }

    return render(request, 'quotation-details.html', context)
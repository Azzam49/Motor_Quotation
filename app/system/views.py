from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from app.features.quotation.models import Quotation
from app.features.vehicle.models import Vehicle
from app.system.models import CustomerProfile

from motor_quotation.tasks import send_email

def login_view(request):
    if request.user.is_authenticated:
        return redirect('quotation-details')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('quotation-details')
        else:
            messages.error(request, 'Username or Password is not correct! Try Again.')

    return render(request, "login.html", { 'title': 'Login' })


def logout_view(request):
    logout(request)
    return render(request, "logout.html", { 'title': 'Logout' })


def send_emails(request):
    for _id in request.POST.get('quotations-id-list').split(','):
        quotation = Quotation.objects.get(id=_id)
        customerprofile = CustomerProfile.objects.get(quotation_id=quotation.pk)

        pdf_data = {
            'username': customerprofile.user.username,
            'email': customerprofile.user.email,
            'mobile': customerprofile.mobile,

            'vehicle_model': quotation.vehicle.model,
            'vehicle_price': quotation.vehicle.price,
            'vehicle_year': quotation.vehicle.year_make,
            'vehicle_number': quotation.vehicle.number,

            'quotation_price': quotation.price,
            'windscreen_coverage': quotation.windscreen_coverage,
            'passenger_liability_coverage': quotation.passenger_liability_coverage,
            'flood_coverage': quotation.flood_coverage,
            'windstorm_coverage': quotation.windstorm_coverage,
            'landslide_coverage': quotation.landslide_coverage,
            'subsidence_coverage':quotation.subsidence_coverage,
        }


        send_email.delay(
            title= 'Quotation PDF File',
            emails_list= [customerprofile.user.email],
            email_template= 'emails/quotation-email.html',
            text_alternative_email= 'emails/quotation-email.txt',
            email_context= {
                'username': customerprofile.user.username,
            },
            has_pdf= True,
            pdf_data= pdf_data,
            pdf_template= 'emails/email-quotation-details.html'
        )

    messages.success(request, 'Emails are send successfully.')
    # return back to admin page
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
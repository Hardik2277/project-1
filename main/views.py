from django.shortcuts import render, redirect
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Contact, Profile


# HOME PAGE
def home(request):
    return render(request, 'home.html')


# RESULT PAGE
def result(request):

    if request.method == "POST":

        number = request.POST.get('number')

        try:

            parsed_number = phonenumbers.parse(number, "IN")

            country = geocoder.description_for_number(parsed_number, "en")

            sim_carrier = carrier.name_for_number(parsed_number, "en")

            timezones = timezone.time_zones_for_number(parsed_number)

            valid = phonenumbers.is_valid_number(parsed_number)

            context = {

                'number': number,
                'country': country,
                'carrier': sim_carrier,
                'timezone': timezones,
                'valid': valid

            }

        except:

            context = {

                'number': number,
                'country': "Invalid",
                'carrier': "Invalid",
                'timezone': "Invalid",
                'valid': False

            }

        return render(request, 'result.html', context)

    return render(request, 'home.html')


# ABOUT PAGE
def about(request):
    return render(request, 'about.html')


# SIGNUP
def signup_view(request):

    if request.method == "POST":

        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()

        if User.objects.filter(username=username).exists():

            return render(request, 'signup.html', {

                'error': 'Username already exists'

            })

        user = User.objects.create_user(

            username=username,
            email=email,
            password=password

        )

        login(request, user)

        return redirect('home')

    return render(request, 'signup.html')


# LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        user = authenticate(request,

            username=username,
            password=password

        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            return render(request, 'login.html', {

                'error': 'Invalid credentials'

            })

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):

    logout(request)

    return redirect('home')


# PROFILE PAGE (NEW)
@login_required
def profile_view(request):

    # Get or create profile for user
    profile, created = Profile.objects.get_or_create(user=request.user)

    # If user uploads image
    if request.method == "POST":

        if request.FILES.get('image'):

            profile.image = request.FILES['image']
            profile.save()

            return redirect('profile')

    # Send profile to template
    return render(request, 'profile.html', {
        'profile': profile
    })

def contact_view(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, 'contact.html', {
            'success': 'Message sent successfully!'
        })

    return render(request, 'contact.html')
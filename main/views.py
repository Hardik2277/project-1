from django.shortcuts import render
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def home(request):
    return render(request, 'home.html')

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

def about(request):
    return render(request, 'about.html')
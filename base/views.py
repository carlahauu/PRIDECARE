from django.shortcuts import render
import googlemaps
import os 
from dotenv import load_dotenv

load_dotenv()

from django.conf import settings


api_key = os.getenv("API_KEY")

def search(request):
    if request.method == 'GET':
        # Get the user's location from the search form
        location = request.GET.get('location')

        # Use the Google Maps Geocoding API to get the latitude and longitude
        gmaps = googlemaps.Client(api_key)
        geocode_result = gmaps.geocode(location)
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']

        # Use the Google Places API to search for healthcare providers near the location
        places_result = gmaps.places_nearby(location=(latitude, longitude),
                                             radius=10000,
                                             type='health, hospitals', 
                                             keyword='lgbtq+ friendly')
        results = places_result['results']

        for result in results:
            place_id = result['place_id']
            place_result = gmaps.place(place_id, fields=['name', 'rating', 'formatted_address', 'photo', 'review'])
            place_details = gmaps.place(place_id)['result']
            reviews = place_details.get('reviews', [])
            result['reviews'] = reviews

        # Render the search results template with the list of providers
        return render(request, 'base/search_results.html', {'results': results})

def home(request): 
  return render(request, 'base/landing.html')

def form(request): 
  return render(request, 'base/forms.html')

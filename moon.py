from app import app  # Importing the 'app' object from a module named 'app'
import ephem
import json
from geopy.geocoders import Nominatim
from calculate_moon_phase import get_moon_phase_name  # Importing a function to calculate moon phase


app = app  # Assigning the 'app' object


@app.post('/moon/phases/{date}/{city}')
def get_moon_phase(date: str, city: str):
    try:
        # Using Geopy to geocode the city name to get coordinates
        geolocator = Nominatim(user_agent="moon_phases")
        location = geolocator.geocode(city)

        # If location is not found, return a 404 error
        if not location:
            return {'error': 'City not found'}, 404

        # Extract latitude and longitude from the location object
        lat = location.latitude
        lon = location.longitude

        # Initialize an ephem Moon object for calculations
        moon = ephem.Moon()

        # Set up an observer with latitude, longitude, and date
        observer = ephem.Observer()
        observer.lat = lat
        observer.lon = lon
        observer.date = date

        # Compute moon phase using ephem
        moon.compute(observer)

        # Get the illuminated fraction of the moon's phase
        illuminated_fraction = moon.phase

        # Convert illuminated fraction to a percentage
        cal = illuminated_fraction / 100

        # Get the moon phase name (e.g., New Moon, Full Moon) using a custom function
        moon_phase_name = get_moon_phase_name(cal)

        # Prepare the result JSON with city coordinates and moon phase information
        result = {
            city: {
                'coordinates': {
                    'latitude': lat,
                    'longitude': lon,
                },
                'moon_phase' : {
                    'date': date,
                    'illuminated_fraction': moon_phase_name
                }
            }
        }

        # Return the result JSON with indented formatting
        return json.dumps(result, indent=4)
    
    # Handle exceptions, such as city not found or other errors
    except Exception as e:
        return {'error': 'City not found'}, 404

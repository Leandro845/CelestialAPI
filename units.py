from app import app  # Importing the 'app' object from a module named 'app'
from astropy import units as u  # Importing the 'units' module from Astropy and aliasing it as 'u'
import json  # Importing the standard Python JSON module for JSON serialization and deserialization

# Assuming 'app' is already defined elsewhere in the 'app' module or framework setup
app = app

# Endpoint for converting parsecs to light years
@app.post('/astronomy/units/parsecs-to-ligthyears/{parsec}')
def convert_parsecs_lightyears(parsec: float):
    # Convert parsecs to light years using Astropy units
    parsecs = parsec * u.parsec
    lightyears = parsecs.to(u.lightyear).value  # Conversion to light years

    # Prepare the result dictionary
    result = {
        "parsecs": parsec,
        "lightyears": round(lightyears)  # Round the light years value for clarity
    }

    # Return the result as JSON with formatted indentation
    return json.dumps(result, indent=4)


# Endpoint for converting degrees to radians
@app.post('/astronomy/units/degrees-to-radians/{degrees}')
def convert_degrees_units(degrees: float):
    # Convert degrees to radians using Astropy units
    radians = degrees * u.deg
    radians = radians.to(u.rad).value  # Conversion to radians

    # Prepare the result dictionary
    result = {
        "degrees": degrees,
        "radians": round(radians)  # Round the radians value for clarity
    }
    
    # Return the result as JSON with formatted indentation
    return json.dumps(result, indent=4)

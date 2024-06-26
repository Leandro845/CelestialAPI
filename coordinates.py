from app import app  # Importing the 'app' object from a module named 'app'
from astropy.coordinates import SkyCoord  # Importing SkyCoord for astronomical coordinate handling
from astropy import units as u  # Importing units module from Astropy and aliasing it as 'u'
from astroquery.simbad import Simbad  # Importing Simbad from astroquery for querying astronomical objects
import json  # Importing the standard Python JSON module for JSON serialization and deserialization


app = app  # Assigning the 'app' object


@app.post('/astronomy/coordinates/region/{ra}/{dec}')
def coordinates_constellation(ra: float, dec: float):
    # Creating SkyCoord object with given RA and Dec in degrees, using ICRS frame
    coord = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
    
    # Getting the constellation region for the given coordinates
    region = coord.get_constellation()

    # Constructing the response JSON object
    response = {
        'right_ascension': coord.ra.deg,
        'declination': coord.dec.deg,
        'region': region
    }

    # Returning the JSON response with indented formatting
    return json.dumps(response, indent=4)


@app.post('/astronomy/coordinates/objects/{ra}/{dec}')
def coordinates_planets(ra: float, dec: float):
    # Creating SkyCoord object with given RA and Dec in degrees, using ICRS frame
    coord = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
    
    # Querying Simbad for astronomical objects within 1 arcsec of the given coordinates
    result_table = Simbad.query_region(coord, radius=1*u.arcsec)
    
    # Getting the constellation region for the given coordinates
    region = coord.get_constellation()

    # Initializing a list to store discovered planets or objects
    planets = []

    # If result_table is not None and contains results, iterate through the table
    if result_table is not None:
        for obj in result_table:
            # Decode MAIN_ID if it's bytes and append to planets list
            main_id = obj['MAIN_ID'].decode('utf-8') if isinstance(obj['MAIN_ID'], bytes) else obj['MAIN_ID']
            planets.append(main_id)

    # Constructing the response JSON object
    response = {
        'region': region,
        'right_ascension': coord.ra.deg,
        'declination': coord.dec.deg,
        'objects': planets
    }

    # Returning the JSON response with indented formatting
    return json.dumps(response, indent=4)


@app.post('/astronomy/coordinates/start_object/{ra}/{dec}')
def coordinates_star_object(ra: float, dec: float):
    # Creating SkyCoord object with given RA and Dec in degrees, using ICRS frame
    coord = SkyCoord(ra=ra*u.degree, dec=dec*u.degree, frame='icrs')
    
    # Querying Simbad for astronomical objects within 1 arcsec of the given coordinates
    result_table = Simbad.query_region(coord, radius=1*u.arcsec)

    # If result_table is not None and contains at least one result
    if result_table is not None and len(result_table) > 0:
        # Get the name of the first star object in the result table
        star_name = result_table['MAIN_ID'][0]

        # Constructing the response JSON object
        response = {
            'right_ascension': coord.ra.deg,
            'declination': coord.dec.deg,
            'star_name': star_name
        }

        # Returning the JSON response with indented formatting
        return json.dumps(response, indent=4)

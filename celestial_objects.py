from app import app  # Importing the 'app' object from a module named 'app'
from astroquery.simbad import Simbad  # Importing Simbad from astroquery for querying astronomical objects
import json  # Importing the standard Python JSON module for JSON serialization and deserialization
import asyncio  # Importing asyncio for asynchronous operations


app = app  # Assigning the 'app' object


async def query_object_async(object_name):
    """
    Asynchronous function to query an astronomical object using Simbad.

    Parameters:
    - object_name (str): The name of the astronomical object to query.

    Returns:
    - result_table: Result table containing information about the queried object.
    """
    loop = asyncio.get_running_loop()  # Get the current event loop
    return await loop.run_in_executor(None, Simbad.query_object, object_name)


@app.post('/celestial_objects/{object_name}')
async def get_celestial_object(object_name):
    """
    Async endpoint to query details of a celestial object by its name.

    Parameters:
    - object_name (str): The name of the celestial object.

    Returns:
    - JSON response containing object name and data retrieved from Simbad.
    """
    task = asyncio.create_task(query_object_async(object_name))  # Create an asyncio task to query the object asynchronously

    result_table = await task  # Wait for the task to complete and get the result

    if result_table is None:
        return {'error': 'Object not found'}, 404  # Return error response if object is not found
    
    # Convert the result table to pandas DataFrame and then to a dictionary of records
    df = result_table.to_pandas()
    result_dict = df.to_dict(orient='records')
    
    # Construct the response JSON object
    result = {
        'object_name': object_name, 
        'data': result_dict
    }
        
    return json.dumps(result, indent=4)  # Return the JSON response with indented formatting

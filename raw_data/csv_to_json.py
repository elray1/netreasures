import pandas as pd
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="netreasures")


def is_nan(x):
    return (x != x)


def safe_str(obj):
    return ('' if is_nan(obj) else str(obj))


def one_row_to_json(i, netreasures):
    result = {
        'name': safe_str(netreasures['Name of Treasure'][i]),
        'street_address': safe_str(netreasures['Street Address'][i]),
        'city': safe_str(netreasures['City'][i]),
        'state': safe_str(netreasures['State'][i]),
        'website': safe_str(netreasures['Web Link'][i]),
        'category': netreasures['Category'][i].split(', '),
        'brief_description': safe_str(netreasures['One-Line Description'][i]),
        'long_description': safe_str(netreasures['Long Description'][i]),
        'tags': netreasures['Tags'][i].split(', '),
        'picture': safe_str(netreasures['Picture'][i])
    }
    
    location = geolocator.geocode(
        result['street_address'] + ' ' + result['city'] + ' ' + result['state'])
    
    result['lat'] = location.latitude
    result['lon'] = location.longitude
    
    return(result)


netreasures = pd.read_csv('raw_data/netreasures.csv')
netreasures_obj = [one_row_to_json(i, netreasures) for i in range(netreasures.shape[0])]



with open('data/netreasures.json', 'w') as f:
    json.dump(netreasures_obj, f)


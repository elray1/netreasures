import pandas as pd
import json

netreasures = pd.read_csv('raw_data/netreasures.csv')

netreasures_obj = [{
    'name': str(netreasures['Name of Treasure'][i]),
    'street_address': str(netreasures['Street Address'][i]),
    'city': str(netreasures['City'][i]),
    'state': str(netreasures['State'][i]),
    'website': str(netreasures['Web Link'][i]),
    'category': netreasures['Category'][i].split(', '),
    'brief_description': netreasures['One-Line Description'][i],
    'long_description': netreasures['Long Description'][i],
    'tags': netreasures['Tags'][i].split(', '),
    'picture': netreasures['Picture'][i]
} for i in range(netreasures.shape[0])]

with open('data/netreasures.json', 'w') as f:
    json.dump(netreasures_obj, f)


import json

def load_data(file_path):
    """Loads JSON data"""
    with open(file_path,"r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')
print (animals_data)
import json


def load_data(file_path):
    """Loads JSON data"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Returns an HTML card string for a single animal"""
    name = animal.get('name', 'N/A')
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet', 'N/A')
    animal_type = characteristics.get('type', 'N/A')
    locations = animal.get('locations', [])
    first_location = locations[0] if locations else 'N/A'
    return (
        '<li class="cards__item">\n'
        f'  <div class="card__title">{name}</div>\n'
        '  <p class="card__text">\n'
        f'    <strong>Diet:</strong> {diet}<br/>\n'
        f'    <strong>Location:</strong> {first_location}<br/>\n'
        f'    <strong>Type:</strong> {animal_type}\n'
        '  </p>\n'
        '</li>'
    )


animals_data = load_data('animals_data.json')
animals_html = '\n'.join(serialize_animal(animal) for animal in animals_data)

with open('animals_template.html', 'r') as f:
    template = f.read()

output = template.replace('__REPLACE_ANIMALS_INFO__', animals_html)

with open('animals.html', 'w') as f:
    f.write(output)

print("animals.html generated successfully.")

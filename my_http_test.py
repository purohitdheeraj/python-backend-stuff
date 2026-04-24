import json
import requests

# Make a GET request to the PokeAPI for Pikachu
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

if response.status_code == 200:
    data = response.json()  # Parse JSON data
    print(data['forms'])  # Output the JSON response
else:
    print(f'Error: {response.status_code}')

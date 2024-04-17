import requests
import json
from urllib.request import urlopen

def is_valid_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False
    
def get_sprite(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    response = requests.get(url)

    json_data = json.loads(response.text)
    # json_data = response.json()
    image = json_data['sprites']['other']['official-artwork']['front_default']
    return image
    # print(image)

    # resource = urlopen(image)
    # output = open("file01.jpg","wb")
    # output.write(resource.read())
    # output.close()
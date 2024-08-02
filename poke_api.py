'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
import os 
import image_lib

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    download_pokemon_artwork= ('dugtrio', r'C:\temp')
    return

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

    # TODO: Define function that gets a list of all Pokemon names from the PokeAPI
def get_pokemon_name(Limit=10000, offset=0):
    print(f'Getting list of Pokemon names....', end='')
    params= {
        'Limit': Limit,
        'offset': offset
    }
    resp_msg=requests.get(POKE_API_URL, params=params)
    if resp_msg.status_code == requests.codes.ok:
        print('Success')
        resp_dict = resp_msg.jsob()
        return[p['name'] for p in resp_dict['results']]
    else:
        print('Failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

    # TODO: Define function that downloads and saves Pokemon artwork

if __name__ == '__main__':
    main()
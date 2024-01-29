import requests

# gets data from get_pokemon.py
def get_pokemon_data(name):
    url = f"http://127.0.0.1:8000/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# print data in terminal
    
pokemon_name = input("Enter pokemon: ").lower()
data = get_pokemon_data(pokemon_name)

if data:
    print("\n___POKEMON DETAILS___")
    print("Name:", data['Name'])
    print("ID:", data['ID'])
    print("Type:", ', '.join(data['Type']))
    print("Sprite:", data['Sprite'])
    print("Height:", data['Height'])
    print("Weight:", data['Weight'])
    print("Abilities:", ', '.join(data['Abilities'])) 
else:
    print("Pokemon not found :(")
    


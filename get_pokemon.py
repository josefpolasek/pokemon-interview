from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get('/pokemon/{name}')
def get_pokemon(name: str):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if response.status_code == 200:
        data = response.json()
        return {
            'Name': data['name'],
            'ID': data['id'],
            'Type': [type['type']['name'] for type in data['types']],
            'Sprite': data['sprites']['front_default'],
            'Height': data['height'],
            'Weight': data['weight'],
            'Abilities': [ability['ability']['name'] for ability in data['abilities']]
        }
    else:
        raise HTTPException(status_code=404, detail="Pokemon not found")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

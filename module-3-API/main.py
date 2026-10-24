import requests
import random

pokemons = ['https://pokeapi.co/api/v2/pokemon/8', 'https://pokeapi.co/api/v2/pokemon/16', 'https://pokeapi.co/api/v2/pokemon/13', 'https://pokeapi.co/api/v2/pokemon/05','https://pokeapi.co/api/v2/pokemon/15']

g = random.choice(pokemons)

x = requests.get(g)

pokemon = [x]

print(f"{pokemon}")
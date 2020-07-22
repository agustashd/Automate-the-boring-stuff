
pokemons = ['pikachu', 'raichu', 'eve', 'nine tails']

for pokemon in range(len(pokemons)):
    print(f'{pokemons[pokemon].capitalize()} finished in {pokemon + 1} position')

for position, pokemon in enumerate(pokemons):
    print(f'{pokemon.capitalize()} finished in {position + 1} position')

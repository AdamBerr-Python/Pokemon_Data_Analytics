import pandas as pd
import requests


user_input = input("Is your Pokemon in Generation 1? (yes/no): ")

while user_input.lower() not in ["yes", "no"]:
    print("Please enter 'yes' or 'no'.")
    user_input = input("Is your Pokemon in Generation 1? (yes/no): ")


def get_pokemon_data(name):

    name = name.lower()

    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{name}"
    )

    if response.status_code != 200:
        return None

    pokemon_data = response.json()

    pokemon_stats = {
        "name": pokemon_data["name"],
        "id": pokemon_data["id"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"]
    }

    for stat in pokemon_data["stats"]:
        pokemon_stats[stat["stat"]["name"]] = stat["base_stat"]

    return pokemon_stats


while True:

    pokemon_input = input("Enter the name of the Pokemon: ")

    if pokemon_input.lower() == "":
        print("Please enter a valid Pokemon name.")
        continue

    pokemon = get_pokemon_data(pokemon_input)

    if pokemon is None:
        print("Pokemon not found. Please try again.")
        continue

    if user_input.lower() == "yes" and pokemon["id"] > 151:
        print("Sorry, this program only supports Generation 1 Pokemon.")
        continue

    print(pokemon)
    break
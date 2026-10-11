#user_input = input('Is your Pokemon in Generation 1? (yes/no): ')


import sys


#while user_input.lower() not in ['yes', 'no']:
#     print("Invalid input. Please enter 'yes' or 'no'.")
#     user_input = input('Is your Pokemon in Generation 1? (yes/no): ')
#     break

# #while user_input.lower() in ['no']:
#     print("Sorry, this program only supports Generation 1 Pokemon.")
#     sys.exit()

import pandas as pd


import requests


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
        "height": str(pokemon_data["height"] / 10),
        "weight": str(pokemon_data["weight"] / 10),
        "types": [t["type"]["name"] for t in pokemon_data["types"]],
    }
    for stat in pokemon_data["stats"]:
        pokemon_stats[stat["stat"]["name"]] = stat["base_stat"]

    return pokemon_stats


#while True:

    pokemon_input = input("Enter the name of the Pokemon: ")

    # if pokemon_input.lower() == "":
    #     print("Please enter a valid Pokemon name.")
    #     continue

    #pokemon = get_pokemon_data(pokemon_input)

    #if pokemon is None:
        #print("Pokemon not found. Please try again.")
        #continue

    #if user_input.lower() == 'yes' and pokemon["id"] > 151:
        #print("Sorry, this program only supports Generation 1 Pokemon.")
        #continue

    #print(pokemon)
    #break

pokemon_gen1_list = []

for pokemon_id in range(1,152):
    pokemon = get_pokemon_data(str(pokemon_id))

    if pokemon is not None:
        pokemon_gen1_list.append(pokemon)

pokemon_ids = [pokemon["id"] for pokemon in pokemon_gen1_list]

Pokemon_gen1_dataframe = pd.DataFrame(pokemon_gen1_list)
Pokemon_gen1_df_cleaned = Pokemon_gen1_dataframe.rename(
    columns={"height": "height (m)",
             "weight": "weight (kg)",
             "special-attack": "special_attack",
             "special-defense": "special_defense"})


import pandas as pd
from pathlib import Path

# Your existing data collection and cleaning code goes here

# Define the Data folder BEFORE saving
project_folder = Path(__file__).resolve().parent.parent
data_folder = project_folder / "Data"

data_folder.mkdir(parents=True, exist_ok=True)

# Save raw Pokémon dataset
Pokemon_gen1_dataframe.to_csv(
    data_folder / "Pokemon_gen1_raw.csv",
    index=False
)

# Save cleaned Pokémon dataset
Pokemon_gen1_df_cleaned.to_csv(
    data_folder / "Pokemon_Gen1_Cleaned.csv",
    index=False
)

print("Raw CSV saved successfully!")
print("Cleaned CSV saved successfully!")
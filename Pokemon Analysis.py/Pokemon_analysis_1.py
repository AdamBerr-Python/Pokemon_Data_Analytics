import pandas as pd
from pathlib import Path

# find project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the cleaned data set
csv_path = project_folder/"Data"/"Pokemon_Gen1_Cleaned.csv"

#Load the dataset
df = pd.read_csv(csv_path)

print(df)

stats_columns = [
    "hp",
    "attack",
    "defense",
    "special_attack",
    "special_defense",
    "speed"
]

df["total_stats"] = df[stats_columns].sum(axis = 1)

#print(df[["name", "total_stats"]].head())

top_10_gen1_pokemon = df.sort_values(
    by = "total_stats",
    ascending = False
).head(10)
#print(top_10_gen1_pokemon[["name", "total_stats"]])

lowest_10_gen1_pokemon = df.sort_values(
    by = "total_stats",
    ascending = True
).head(10)
#print(lowest_10_gen1_pokemon[["name", "total_stats"]])

mean_gen1_total_stats = df["total_stats"].mean()
#print(mean_gen1_total_stats)

gen1_pokemon_above_500_total_stats = df[df["total_stats"] > 500].sort_values(
    by = "total_stats",
    ascending = False
)
#print(gen1_pokemon_above_500_total_stats[["name", "total_stats"]])

# calculate the average of each total base stat for all generation 1 Pokémon
average_stats = df[stats_columns].mean()
#print(average_stats)

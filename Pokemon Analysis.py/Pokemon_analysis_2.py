import pandas as pd
from pathlib import Path

# find project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the cleaned data set
csv_path = project_folder/"Data"/"Pokemon_Gen1_Cleaned.csv"

#Load the dataset
df = pd.read_csv(csv_path)

stats_columns = [
    "hp",
    "attack",
    "defense",
    "special_attack",
    "special_defense",
    "speed"
]

df["total_stats"] = df[stats_columns].sum(axis = 1)


top_10_gen1_pokemon = df.sort_values(
    by = "total_stats",
    ascending = False
).head(10)

lowest_10_gen1_pokemon = df.sort_values(
    by = "total_stats",
    ascending = True
).head(10)

mean_gen1_total_stats = df["total_stats"].mean()

gen1_pokemon_above_500_total_stats = df[df["total_stats"] > 500].sort_values(
    by = "total_stats",
    ascending = False
)

# calculate the average of each total base stat for all generation 1 Pokémon
average_stats = df[stats_columns].mean()


# convert types back to list instead of strings
import ast
df["types"] = df["types"].apply(ast.literal_eval)
print(df["types"].head())

# seperate the list so that a pokemon with multiples
# types will come up twice, one for each type
types_df = df.explode("types")

print(types_df[["name", "types", "attack"]].head(10))

# Calculateing average attack by type
average_attack_by_type = (types_df.groupby("types")["attack"]
                                          .mean()
                                          .sort_values(ascending = False)
)
print(average_attack_by_type)
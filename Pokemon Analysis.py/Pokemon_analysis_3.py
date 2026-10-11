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

# seperate the list so that a pokemon with multiples
# types will come up twice, one for each type
types_df = df.explode("types")

# Calculateing average attack by type
average_attack_by_type = (types_df.groupby("types")["attack"]
                                          .mean()
                                          .sort_values(ascending = False)
)

# Analysing multiple stats at the same time using agg()
types_analysis = (
    types_df.groupby("types")
    .agg(
        pokemon_count = ("id", "count"),
        average_hp = ("hp", "mean"),
        average_attack = ("attack", "mean"),
        average_defense = ("defense", "mean"),
        average_special_attack = ("special_attack", "mean"),
        average_special_defense = ("special_defense", "mean"),
        average_speed = ("speed", "mean"),
        average_total_stats = ("total_stats", "mean")
    )
    .round(2)
    .sort_values("average_total_stats",
                 ascending = False)
                 )

print(types_analysis)

#print(types_analysis.info())
#print(types_analysis.describe().round(2))
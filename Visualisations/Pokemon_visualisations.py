import pandas as pd
from pathlib import Path
import numpy as np

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

import matplotlib.pyplot as plt

def average_total_stats_by_type_figure():
    plt.figure(figsize = (14, 8))

    bars = plt.barh(
        types_analysis.index,
        types_analysis["average_total_stats"],
        color = 'steelblue',
        edgecolor = 'black'
    )
    plt.bar_label(bars, 
            color = 'black')
    plt.xlabel("Average Total Base Stats", 
            color = 'black')
    plt.ylabel("Pokemon Type", 
            color = 'black')
    plt.title("Average Total Base Stats by type", 
            color = 'black', 
            alpha = 1,  
            fontsize = 20)
    # put highest rank at the top
    plt.gca().invert_yaxis()
    #improve spacing
    plt.tight_layout()

    project_folder = Path(__file__).resolve().parent.parent
    visualisations_folder = project_folder / "Visualisations"

    visualisations_folder.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        visualisations_folder / "average_stats_by_type.png",
        dpi=300,
        bbox_inches="tight"
    )
    return plt.show()
#average_total_stats_by_type_figure()

def top_10_figure():
    plt.figure(figsize = (14, 7))
    top_10_gen1_pokemon = df.sort_values(
    by = "total_stats",
    ascending = False
    ).head(10)
    top_10_gen1_graph = plt.barh(
        top_10_gen1_pokemon.name,
        top_10_gen1_pokemon["total_stats"],
        color = 'darkgreen',
        edgecolor = 'black'
    )
    plt.bar_label(top_10_gen1_graph,
        color = 'black'
    )
    plt.xlabel("Total Base Stats",
               color = 'black'
    )
    plt.ylabel("Pokemon Index Number",
               color = 'black'
    )
    plt.title("Top 10 Pokemon By Total Base Stats",
              color = 'black',
              fontsize = '15',
              alpha = 1
    )
    plt.gca().invert_yaxis()
    plt.tight_layout()

    project_folder = Path(__file__).resolve().parent.parent
    visualisations_folder = project_folder / "Visualisations"
    
    visualisations_folder.mkdir(parents=True, exist_ok=True)
    
    plt.savefig(
            visualisations_folder / "Top_10_Pokemon_by_Total_Base_Stats.png",
            dpi=300,
            bbox_inches="tight"
        )

    return plt.show()

#top_10_figure()

def avg_attack_vs_avg_speed_figure():
    plt.figure(figsize = (14, 7))
    plt.scatter(
        types_analysis["average_attack"],
        types_analysis["average_speed"]
    )
    plt.xlabel("Average Attack",
               color = 'black'
    )
    plt.ylabel("Average Speed",
               color = 'black'
    )
    plt.title("Average attack Vs Speed",
              color = 'black',
              fontsize = 15,
              alpha = 1
    )
    plt.tight_layout()

    return plt.show()



def attack_vs_speed_figure():
    plt.figure(figsize = (14, 7))
    df[stats_columns]
    plt.scatter(
        df[stats_columns]["attack"],
        df[stats_columns]["speed"],
        color = 'darkgreen'
    )
    plt.xlabel("attack",
               color = 'black'
    )
    plt.ylabel("speed",
               color = 'black')
    plt.title("Attack VS Speed (Gen 1 - 151 Pokemon)",
              color = 'black',
              fontsize = 15,
              alpha = 1
    )
    plt.tight_layout()

    #line of best fit
    slope, intercept = np.polyfit(df[stats_columns]["attack"], df[stats_columns]["speed"], 1)
    predicted_speed = slope * df[stats_columns]["attack"] + intercept
    #generating evenly spaced attack values in order
    attack_line = np.linspace(
        df[stats_columns]["attack"].min(),
        df[stats_columns]["attack"].max(),
        100
    )
    speed_line = slope * attack_line + intercept 
    plt.plot(attack_line, speed_line,
             color = 'black',
             linestyle = '--',
             linewidth = 2,
             label = 'Line of best fit'
    )

    plt.legend()

    print(
        (df[stats_columns]["attack"]).corr(df[stats_columns]["speed"])
    )

    project_folder = Path(__file__).resolve().parent.parent
    visualisations_folder = project_folder / "Visualisations"
        
    visualisations_folder.mkdir(parents=True, exist_ok=True)
        
    plt.savefig(
            visualisations_folder / "Attack_vs_speed.png",
            dpi=300,
            bbox_inches="tight"
    )
    
    return plt.show()

attack_vs_speed_figure()
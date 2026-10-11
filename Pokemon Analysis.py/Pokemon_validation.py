
import pandas as pd
import sqlite3
import ast
from pathlib import Path

# Locate project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate existing files
csv_path = project_folder / "Data" / "Pokemon_Gen1_Cleaned.csv"
db_path = project_folder / "SQL" / "pokemon_gen1.db"

# Load the CSV
df = pd.read_csv(csv_path)

# Connect to SQLite
connection = sqlite3.connect(db_path)


# Pandas count
pandas_count = len(df)

# SQL count
sql_count = pd.read_sql_query(
    "SELECT COUNT(*) AS total FROM pokemon",
    connection
)["total"].iloc[0]

print("Pandas Pokémon count:", pandas_count)
print("SQL Pokémon count:", sql_count)
print("Counts match:", pandas_count == sql_count)


# Convert saved type lists back into Python lists
df["types"] = df["types"].apply(ast.literal_eval)

# Separate dual-type Pokémon
types_df = df.explode("types")

# Calculate Pandas averages
pandas_averages = (
    types_df.groupby("types")["attack"]
    .mean()
    .sort_index()
)

# done with AI as I have not learnt this

sql_averages = pd.read_sql_query(
    """
    SELECT
        pokemon_types.type,
        AVG(pokemon.attack) AS average_attack
    FROM pokemon
    INNER JOIN pokemon_types
        ON pokemon.id = pokemon_types.pokemon_id
    GROUP BY pokemon_types.type
    """,
    connection
).set_index("type")["average_attack"].sort_index()

import numpy as np

averages_match = (
    pandas_averages.index.equals(sql_averages.index)
    and np.allclose(pandas_averages.values, sql_averages.values)
)

print("Type averages match:", averages_match)


stat_columns = [
    "hp", "attack", "defense",
    "special_attack", "special_defense", "speed"
]

# Pandas ranking
df["total_stats"] = df[stat_columns].sum(axis=1)

pandas_top10 = (
    df.sort_values(
        ["total_stats", "id"],
        ascending=[False, True]
    )
    .head(10)[["id", "total_stats"]]
    .reset_index(drop=True)
)

# SQL ranking
sql_top10 = pd.read_sql_query(
    """
    SELECT
        id,
        hp + attack + defense +
        special_attack + special_defense + speed
        AS total_stats
    FROM pokemon
    ORDER BY total_stats DESC, id ASC
    LIMIT 10
    """,
    connection
)

print("Top 10 rankings match:",
      pandas_top10.equals(sql_top10))


# Count dual-type Pokémon in Pandas
pandas_dual = (df["types"].apply(len) == 2).sum()

# Count dual-type Pokémon in SQL
sql_dual = pd.read_sql_query(
    """
    SELECT COUNT(*) AS total
    FROM (
        SELECT pokemon_id
        FROM pokemon_types
        GROUP BY pokemon_id
        HAVING COUNT(DISTINCT type) = 2
    )
    """,
    connection
)["total"].iloc[0]

print("Pandas dual-type count:", pandas_dual)
print("SQL dual-type count:", sql_dual)
print("Dual-type counts match:", pandas_dual == sql_dual)

connection.close()

import sqlite3
import pandas as pd
from pathlib import Path

# Locate your project folder
project_folder = Path(__file__).resolve().parent.parent

# Locate the cleaned CSV
csv_path = project_folder / "Data" / "Pokemon_Gen1_Cleaned.csv"

# Choose where the database will be saved
database_path = project_folder / "SQL" / "pokemon_gen1.db"

# Load the CSV into Pandas
df = pd.read_csv(csv_path)

# Create or connect to the SQLite database
connection = sqlite3.connect(database_path)

df.to_sql(
    name = "pokemon",
    con = connection,
    if_exists = "replace",
    index = False
)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM pokemon")

print("Pokemon in database:", cursor.fetchone()[0])


import ast

# Creates a separate DataFrame containing IDs and types
pokemon_types = df[["id", "types"]].copy()

# Converts the text representations into Python lists
pokemon_types["types"] = pokemon_types["types"].apply(
    ast.literal_eval
)

# Separates dual-type Pokémon into individual rows
pokemon_types = pokemon_types.explode("types")

# Renames columns
pokemon_types = pokemon_types.rename(
    columns={
        "id": "pokemon_id",
        "types": "type"
    }
)

print(pokemon_types.head(10))


pokemon_types.to_sql(
    name = "pokemon_types",
    con = connection,
    if_exists = "replace",
    index = False
)

connection.close()
# Pokémon Generation 1 — Data Analytics Project

## Project Overview

An end-to-end data analytics project exploring the original 151 Generation 1 Pokémon using Python, Pandas, Matplotlib, NumPy and SQLite.

The project demonstrates practical experience in API data extraction, data cleaning, exploratory data analysis, statistical analysis, data visualisation and relational database querying.

**Data Source:** [PokéAPI](https://pokeapi.co/)

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data collection and processing |
| Requests / PokéAPI | Retrieving Pokémon data from an external API |
| Pandas | Data cleaning, manipulation and exploratory analysis |
| NumPy | Regression calculations |
| Matplotlib | Data visualisation |
| SQLite | Database management and SQL queries |
| VS Code | Development environment |

## Project Workflow

### 1. Data Collection

- Retrieved information for all 151 original Pokémon using PokéAPI.
- Extracted Pokémon names, Pokédex IDs, types, height, weight and six base stats.
- Constructed a structured dataset using Python dictionaries and Pandas.
(As a note: Initial Project Idea was a Pokémon recommender, hence the Pokémon finder file under Pokemon Project.py,
I will still be continuing this project on the side, but I had to prioritise Data Visualisation and SQL for my data 
analytics application.)

### 2. Data Cleaning and Validation

- Standardised column names and converted height and weight into numerical values.
- Checked for missing values, duplicate Pokémon and inconsistent IDs.
- Preserved separate raw and cleaned CSV datasets.
- Compared key results across Pandas and SQLite to assess consistency.

### 3. Exploratory Data Analysis

Used Pandas to investigate:

- Rankings of Pokémon by total base stats.
- Average statistics across Pokémon types.
- Differences in sample sizes between types.
- Relationships between Attack and Speed.

### 4. Data Visualisation and Statistical Analysis

Created Matplotlib visualisations including:

- Average total base stats by Pokémon type.
- Top 10 Pokémon ranked by total base stats.
- Attack versus Speed scatter plots, including a linear regression line.

Calculated Pearson correlation coefficients to investigate linear relationships.

### 5. SQL Database and Analysis

- Imported the cleaned dataset into a SQLite database.
- Created separate `pokemon` and `pokemon_types` tables.
- Used `INNER JOIN`, `GROUP BY`, `HAVING`, `COUNT`, `AVG` and `ORDER BY` for data analysis.
- Investigated dual-type Pokémon, type distributions and statistical rankings.

## Visualisations

### Average Total Base Stats by Type

![Average Stats by Type](Visualisations/average_stats_by_type.png)

### Top 10 Pokémon by Total Base Stats

![Top 10 Pokémon](Visualisations/Top_10_Pokemon_by_Total_Base_Stats.png)

### Attack vs Speed

![Attack vs Speed](Visualisations/Attack_vs_speed.png)

## Findings and Limitations

The analysis examines the relationship between Pokémon types, base stats and individual stat distributions.

Important limitations include:

- Some Pokémon types have relatively small sample sizes.
- Dual-type Pokémon contribute to multiple type-level averages.
- Correlation does not establish causation.
- Base stats alone do not fully determine competitive battle performance.

See [Findings.md](Findings.md) for detailed observations and interpretations.

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/YOUR_USERNAME/Pokemon-Data-Analytics.git
cd Pokemon-Data-Analytics
python -m pip install -r requirements.txt
```

Replace `YOUR_USERNAME` with your GitHub username.

## Project Structure

```text
Pokemon Project Folder/
├── Data/
├── Pokemon Analysis.py/
├── Pokemon Project.py/
├── SQL/
├── Visualisations/
├── .gitignore
├── Findings.md
├── README.md
└── requirements.txt
```

The `Data` folder contains the raw and cleaned datasets. The analysis and project folders contain Python scripts, while the SQL folder contains the SQLite database and SQL queries. The visualisation folder contains the generated charts.

## Future Improvements

- Extend the dataset to later Pokémon generations.
- Explore additional statistical relationships.
- Build an interactive dashboard.
- Expand SQL queries and database normalisation.
(And completing my Pokémon recommender)

## Acknowledgements

Pokémon data is provided by [PokéAPI](https://pokeapi.co/). Pokémon and related intellectual property belong to their respective owners. This project was developed independently for educational and portfolio purposes.
import pandas as pd
from sqlalchemy import create_engine

# 1. Crear la conexión a la base de datos (ejemplo SQLite)
engine = create_engine('sqlite:///mi_base_de_datos.db')

# 2. Definir la consulta SQL
query = "SELECT columna1, columna2 FROM mi_tabla WHERE columna1 > 10"

# 3. Crear el DataFrame
df = pd.read_sql_query(query, engine)

df = pd.set_option('display.max_rows', None)


# Basic save (includes index by default)
df.to_csv('filename.csv')

# Recommended save (excludes the row index for a cleaner file)
df.to_csv('filename.csv', index=False)

print(df.head())
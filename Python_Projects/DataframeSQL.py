import pandas as pd
from sqlalchemy import create_engine

# 1. Configurar la conexión (reemplaza con tus credenciales)
#engine = create_engine('postgresql://usuario:contraseña@localhost:5432/nombre_db')
engine = create_engine('mssql+pyodbc://@NOMBRE_DE_TU_PC/NOMBRE_BD?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes')

#2. Crear la consulta SQL
query = "SELECT * FROM nombre_tabla"
df = pd.read_sql(query, engine)

# 2. Crear el csv
df.to_csv('primer_intento.csv')

df.to_csv('primer_intento', index=False)

# 3. Mostrar el DataFrame
print(df.head())
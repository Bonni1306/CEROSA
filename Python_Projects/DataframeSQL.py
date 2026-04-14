import pandas as pd
from sqlalchemy import create_engine

# 1. Configurar la conexión (reemplaza con tus credenciales)
engine = create_engine('postgresql://usuario:contraseña@localhost:5432/nombre_db')

query = "SELECT * FROM nombre_tabla"
df = pd.read_sql(query, engine)

# 3. Mostrar el DataFrame
print(df.head())



#hola mundo
import pandas as pd
from Database import get_connection

def consultar_datos():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Ejemplo de consulta simple
            cursor.execute("SELECT TOP 10 * FROM MiTabla")
            
            # Recuperar los nombres de las columnas
            columns = [column[0] for column in cursor.description]
            
            # Crear una lista de diccionarios para que sea fácil de leer
            resultados = []
            for row in cursor.fetchall():
                resultados.append(dict(zip(columns, row)))
            
            return resultados
        except Exception as e:
            print(f"Error en la consulta: {e}")
        finally:
            conn.close() # Siempre cierra la conexión
    return []

def buscar_por_id(id_busqueda):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Usamos parámetros (?) para evitar Inyección SQL
            query = "SELECT * FROM MiTabla WHERE Id = ?"
            cursor.execute(query, (id_busqueda,))
            
            row = cursor.fetchone()
            return row
        finally:
            conn.close()

def exportar_usuarios_a_csv(nombre_archivo="datos_SQL.csv"):
    conn = get_connection()
    if conn:
        try:
            query = "SELECT * FROM Usuarios"
            
            # 1. Crear el DataFrame directamente desde el query
            # Pandas lee la conexión y ejecuta el SQL por ti
            df = pd.read_sql(query, conn)
            
            # 2. Transformar el DataFrame en un CSV
            # index=False evita que se guarde una columna extra con los números de fila
            df.to_csv(nombre_archivo, index=False, encoding='utf-8')
            
            print(f"Éxito: Archivo '{nombre_archivo}' creado con {len(df)} registros.")
            return df
            
        except Exception as e:
            print(f"Error al procesar datos o crear CSV: {e}")
        finally:
            conn.close()
    return None
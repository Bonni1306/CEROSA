from repository import consultar_datos, buscar_por_id

def run():
    print("Obteniendo datos...")
    registros = consultar_datos()
    
    for r in registros:
        print(r)

if __name__ == "__main__":
    run()
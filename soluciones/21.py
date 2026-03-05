from utils import cargar_y_limpiar

def solucionar():
    # 1. Cargamos los datos con tu limpieza maestra
    df = cargar_y_limpiar()
    
    # 2. Filtramos: cualquier fecha menor estrictamente al 1 de enero de 1960
    # Pandas maneja la comparación de objetos datetime de forma nativa
    antes_de_1960 = df[df['fecha_limpia'] < '1960-01-01']
    
    # 3. Contamos los registros
    resultado = len(antes_de_1960)
    
    print(f"{resultado}")
    return resultado

if __name__ == "__main__":
    solucionar()
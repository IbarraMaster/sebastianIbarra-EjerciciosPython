from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Contamos valores únicos en la columna ya normalizada
    cantidad_unicas = df['profesion'].nunique()
    
    print(f"{cantidad_unicas}")
    return cantidad_unicas

if __name__ == "__main__":
    solucionar()
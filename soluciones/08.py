from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # nunique() cuenta los valores distintos en la columna ya limpia
    cantidad_unicas = df['ciudad'].nunique()
    
    print(f"{cantidad_unicas}")
    return cantidad_unicas

if __name__ == "__main__":
    solucionar()
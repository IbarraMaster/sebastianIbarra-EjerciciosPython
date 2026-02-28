from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Filtramos por Medellin o Medellín
    filtro_medellin = df['ciudad'].str.contains(r'Medell[ií]n', case=False, na=False)
    cantidad = df[filtro_medellin].shape[0]
    
    print(f"{cantidad}")
    return cantidad

if __name__ == "__main__":
    solucionar()
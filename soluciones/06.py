from utils import cargar_y_limpiar

def solucionar():
    # 1. Cargamos el dataset con la limpieza de símbolos (@, #, *, etc.)
    df = cargar_y_limpiar()
    
    # 2. Buscamos "Bogota"
    # Usamos un filtro que ignore mayúsculas/minúsculas y, por seguridad, 
    # que acepte tanto "Bogota" como "Bogotá" (si es que existe con tilde)
    
    # .str.contains con regex 'Bogot[aá]' busca Bogota o Bogotá
    filtro_bogota = df['ciudad'].str.contains(r'Bogot[aá]', case=False, na=False)
    cantidad = df[filtro_bogota].shape[0]
    
    print(f"{cantidad}")
    return cantidad

if __name__ == "__main__":
    solucionar()
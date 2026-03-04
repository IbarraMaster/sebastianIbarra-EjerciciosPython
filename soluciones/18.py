from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Contamos los registros donde activo_bool es False
    # Usamos el operador ~ (not) o comparamos directamente con False
    inactivos = len(df[df['activo_bool'] == False])
    
    print(f"{inactivos}")
    return inactivos

if __name__ == "__main__":
    solucionar()
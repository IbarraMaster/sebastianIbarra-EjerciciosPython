from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Filtro doble: Nombre y Profesión (usando tu PROFESION_MAP de utils)
    filtro = (df['nombre'] == 'Ana') & (df['profesion'] == 'Medico')
    resultado = len(df[filtro])
    
    print(f"{resultado}")
    return resultado

if __name__ == "__main__": solucionar()
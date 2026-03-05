from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Filtro doble: Nombre exacto y Ciudad exacta (ya normalizados a Title case)
    filtro = (df['nombre'] == 'Carlos') & (df['ciudad'] == 'Cali')
    resultado = len(df[filtro])
    
    print(f"{resultado}")
    return resultado

if __name__ == "__main__": solucionar()
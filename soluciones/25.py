from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Filtro: Profesión exacta y Salario estrictamente mayor a 10M
    filtro = (df['profesion'] == 'Abogado') & (df['salario_limpio'] > 10000000)
    
    resultado = len(df[filtro])
    print(f"{resultado}")
    return resultado

if __name__ == "__main__": 
    solucionar()
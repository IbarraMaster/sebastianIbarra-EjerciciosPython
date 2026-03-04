from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Buscamos el máximo en la columna ya filtrada
    maximo = df['salario_limpio'].max()
    
    resultado = int(maximo)
    print(f"{resultado}")
    return resultado

if __name__ == "__main__":
    solucionar()
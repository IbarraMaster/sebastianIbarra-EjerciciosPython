from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    # Contamos los True en la columna que normalizaste en el paso 6 del utils
    resultado = df['activo_bool'].sum()
    print(f"{resultado}")
    return resultado

if __name__ == "__main__":
    solucionar()
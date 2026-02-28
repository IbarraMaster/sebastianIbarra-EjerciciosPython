from utils import cargar_y_limpiar

def solucionar():
    # Cargamos el dataset ya limpio (sin símbolos ni errores de ROT13)
    df = cargar_y_limpiar()
    
    # Obtenemos el conteo de cada nombre
    conteo_nombres = df['nombre'].value_counts()
    
    # El nombre más frecuente es el índice del primer elemento (el más alto)
    nombre_top = conteo_nombres.idxmax()
    
    # La cantidad de veces es el valor máximo
    cantidad_top = conteo_nombres.max()
    
    # El formato que pide el taller suele ser "Nombre Cantidad" o similar
    # Imprimimos el resultado exacto
    print(f"{nombre_top} {cantidad_top}")
    
    return f"{nombre_top} {cantidad_top}"

if __name__ == "__main__":
    solucionar()
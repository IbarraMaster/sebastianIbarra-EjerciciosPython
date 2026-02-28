from utils import cargar_y_limpiar

def solucionar():
    # Cargamos el dataset limpio (nombres y apellidos descifrados y sin símbolos)
    df = cargar_y_limpiar()
    
    # Contamos la frecuencia de cada apellido
    conteo_apellidos = df['apellido'].value_counts()
    
    # Obtenemos el apellido con más apariciones
    apellido_top = conteo_apellidos.idxmax()
    
    # Obtenemos el número de veces que aparece
    cantidad_top = conteo_apellidos.max()
    
    # Imprimimos el resultado (Ejemplo: Garcia 15234)
    resultado = f"{apellido_top} {cantidad_top}"
    print(resultado)
    
    return resultado

if __name__ == "__main__":
    solucionar()
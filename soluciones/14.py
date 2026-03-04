from utils import cargar_y_limpiar

def solucionar():
    # Cargamos datos pasando por la limpieza de utils.py
    df = cargar_y_limpiar()
    
    # Filtramos los que son > 0 para no promediar los errores que descartamos
    salarios_validos = df[df['salario_limpio'] > 0]['salario_limpio']
    
    promedio = salarios_validos.mean()
    
    # Lo convertimos a entero para el reporte final
    resultado = int(promedio)
    
    print(f"{resultado}")
    return resultado

if __name__ == "__main__":
    solucionar()
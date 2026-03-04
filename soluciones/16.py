from utils import cargar_y_limpiar

def solucionar():
    # 1. Cargamos el DataFrame con la limpieza de utils
    df = cargar_y_limpiar()
    
    # 2. Filtramos para ignorar los 0.0 (errores o nulos)
    # Solo queremos salarios mayores a cero
    salarios_reales = df[df['salario_limpio'] > 0]['salario_limpio']
    
    # 3. Obtenemos el valor más bajo de esos salarios reales
    minimo = salarios_reales.min()
    
    # Convertimos a entero para el reporte
    resultado = int(minimo)
    
    print(f"{resultado}")
    return resultado

if __name__ == "__main__":
    solucionar()
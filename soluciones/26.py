from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Triple condición:
    # 1. Ciudad (normalizada por tu mapa a 'Barranquilla')
    # 2. Activo (tu columna activo_bool)
    # 3. Nacidos después de 1980 (del 1 de enero de 1981 en adelante)
    condicion = (
        (df['ciudad'] == 'Barranquilla') & 
        (df['activo_bool'] == True) & 
        (df['fecha_limpia'] > '1980-12-31')
    )
    
    resultado = len(df[condicion])
    print(f"{resultado}")
    return resultado

if __name__ == "__main__": 
    solucionar()
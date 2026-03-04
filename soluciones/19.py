import re
from utils import cargar_y_limpiar

def solucionar():
    # 1. Cargamos el DataFrame
    df = cargar_y_limpiar()
    
    # 2. Definimos el patrón correcto: YYYY-MM-DD
    # ^ (inicio), \d{4} (4 números), - (guion), etc.
    patron_correcto = r'^\d{4}-\d{2}-\d{2}$'
    
    # 3. Filtramos los que NO coinciden con el patrón
    # Usamos .astype(str) para evitar errores con valores nulos
    incorrectos = df[~df['fecha_nacimiento'].astype(str).str.match(patron_correcto)]
    
    total_incorrectos = len(incorrectos)
    
    print(f"{total_incorrectos}")
    return total_incorrectos

if __name__ == "__main__":
    solucionar()
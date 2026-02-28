import pandas as pd
import os

def solucionar():
    path = os.path.join('.', 'data', 'personas.csv')
    df = pd.read_csv(path)
    
    # Convertimos a string y quitamos nulos para el análisis
    salario_raw = df['salario'].astype(str)
    
    # Buscamos cualquier cosa que NO sea un número puro. 
    # La regex ^\d+$ significa: desde el inicio hasta el fin solo puede haber dígitos.
    # Usamos ~ para obtener los que NO cumplen esa regla.
    sucios = df[~salario_raw.str.match(r'^\d+$', na=False)]
    
    resultado = len(sucios)
    print(f"{resultado}")
    return resultado

if __name__ == "__main__":
    solucionar()
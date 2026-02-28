import pandas as pd
import os

def solucionar():
    path = os.path.join('.', 'data', 'personas.csv')
    
    # Leemos el archivo original
    df = pd.read_csv(path)
    
    # Convertimos a string para asegurar que podemos comparar
    email_original = df['email'].astype(str)
    
    # Un email tiene espacios adicionales si es diferente a su versión con .strip()
    # .strip() elimina espacios, tabs (\t) y saltos de línea (\n) de los extremos
    con_espacios = email_original[email_original != email_original.str.strip()]
    
    resultado = len(con_espacios)
    print(f"{resultado}")
    
    return resultado

if __name__ == "__main__":
    solucionar()
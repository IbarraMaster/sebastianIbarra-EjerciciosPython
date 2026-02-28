import pandas as pd
import os

def solucionar():
    path = os.path.join('.', 'data', 'personas.csv')
    df = pd.read_csv(path, dtype={'id': str})
    
    # Buscamos IDs que tengan cualquier cosa que NO sea un número
    # La regex \D busca "cualquier carácter que no sea un dígito"
    no_numericos = df[df['id'].str.contains(r'\D', na=False)]
    
    resultado = len(no_numericos)
    print(f"{resultado}")
    return resultado

if __name__ == "__main__":
    solucionar()
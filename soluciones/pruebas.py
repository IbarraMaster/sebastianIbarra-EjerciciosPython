#Este archivo es temporal y solo se usa para hacer pruebas rapidas. No forma parte de la solución final.

import pandas as pd

# Cargar el dataset
df = pd.read_csv('./data/personas.csv')  # O el formato que estés utilizando

# Ver los primeros 10 registros con todas sus columnas
print(df.shape)
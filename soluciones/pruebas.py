import pandas as pd

# Cargar el dataset
df = pd.read_csv('./data/personas.csv')  # O el formato que estés utilizando

# Ver los primeros 10 registros con todas sus columnas
print(df.head(20))
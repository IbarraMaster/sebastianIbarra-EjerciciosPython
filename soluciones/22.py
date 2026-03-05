from utils import cargar_y_limpiar
import pandas as pd

def solucionar():
    df = cargar_y_limpiar()
    
    # Fecha de corte: 2026-02-26 menos 50 años
    fecha_limite = pd.Timestamp('1976-02-26')
    
    # Si nació ANTES de esa fecha, ya cumplió o pasó los 50 años
    mayores_50 = df[df['fecha_limpia'] < fecha_limite]
    
    resultado = len(mayores_50)
    
    print(f"{resultado}")
    return resultado

if __name__ == "__main__":
    solucionar()
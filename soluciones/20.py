from utils import cargar_y_limpiar

def solucionar():
    # 1. Cargamos el DataFrame con la fecha ya normalizada
    df = cargar_y_limpiar()
    
    # 2. Filtramos el rango (inclusive 1990 y 2000)
    # Pandas entiende los strings 'YYYY-MM-DD' al comparar con datetimes
    mascara = (df['fecha_limpia'] >= '1990-01-01') & (df['fecha_limpia'] <= '2000-12-31')
    
    # 3. Contamos cuántos registros cumplen la condición
    conteo = df[mascara].shape[0]
    
    print(f"{conteo}")
    return conteo

if __name__ == "__main__":
    solucionar()
from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    filtro = (df['nombre'] == 'Jose') & (df['apellido'] == 'Garcia')
    resultado = len(df[filtro])
    print(f"{resultado}")
    return resultado

if __name__ == "__main__": solucionar()
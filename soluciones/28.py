from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    # Agrupamos y sacamos el promedio, luego ordenamos de mayor a menor
    promedios = df.groupby('profesion')['salario_limpio'].mean().sort_values(ascending=False)
    resultado = promedios.idxmax()
    print(f"{resultado}")
    return resultado

if __name__ == "__main__": solucionar()
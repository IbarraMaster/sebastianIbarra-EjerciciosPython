from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    ingenieros = df[df['profesion'] == 'Ingeniero']
    resultado = ingenieros['ciudad'].value_counts().idxmax()
    print(f"{resultado}")
    return resultado

if __name__ == "__main__": solucionar()
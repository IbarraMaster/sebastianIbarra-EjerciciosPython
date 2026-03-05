from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    # Buscamos los que terminan en @gmail.com
    gmails = df[df['email_limpio'].str.endswith('gmail.com')]
    resultado = len(gmails)
    print(f"{resultado}")
    return resultado

if __name__ == "__main__": solucionar()
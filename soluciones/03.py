from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    cantidad = df[df['nombre'] == 'Juan'].shape[0]
    print(f"{cantidad}")
    return cantidad

if __name__ == "__main__":
    solucionar()
from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    # Ahora que utils.py limpia todo, "Maria" saldrá perfecto
    cantidad = df[df['nombre'] == 'Maria'].shape[0]
    print(f"{cantidad}")
    return cantidad

if __name__ == "__main__":
    solucionar()
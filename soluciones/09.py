from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Buscamos "Ingeniero"
    # Gracias a utils.py, '@Ingeniero' ahora es 'Ingeniero'
    cantidad = df[df['profesion'] == 'Ingeniero'].shape[0]
    
    print(f"{cantidad}")
    return cantidad

if __name__ == "__main__":
    solucionar()
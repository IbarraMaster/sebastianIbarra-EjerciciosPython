from utils import cargar_y_limpiar

def solucionar():
    df = cargar_y_limpiar()
    
    # Buscamos "Programador"
    cantidad = df[df['profesion'] == 'Programador'].shape[0]
    
    print(f"{cantidad}")
    return cantidad

if __name__ == "__main__":
    solucionar()
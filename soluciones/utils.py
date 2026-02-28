import pandas as pd
import codecs
import re

def cargar_y_limpiar():
    # 1. Leer datos
    df = pd.read_csv('./data/personas.csv')

    # 2. Descifrar nombres y apellidos (ROT13) y limpiar basura
    def descifrar_y_limpiar(texto):
        if pd.isna(texto): return ""
        descifrado = codecs.decode(str(texto), 'rot_13')
        # Quitar cualquier cosa que no sea letra o espacio
        return re.sub(r'[^a-zA-Z\s]', '', descifrado).strip().title()

    df['nombre'] = df['nombre_cifrado'].apply(descifrar_y_limpiar)
    df['apellido'] = df['apellido_cifrado'].apply(descifrar_y_limpiar)

    # 3. Limpiar Ciudades y Profesiones
    def limpiar_texto_general(texto):
        if pd.isna(texto): return ""
        # Quitar símbolos como @, %, #, *, !, (, ), \t
        limpio = re.sub(r'[@%#*!()\t]', '', str(texto))
        return limpio.strip().title()

    df['ciudad'] = df['ciudad'].apply(limpiar_texto_general)
    df['profesion'] = df['profesion'].apply(limpiar_texto_general)

    # 4. Limpiar Salarios (Solo dejar números)
    def limpiar_salario(valor):
        # Quitar todo lo que no sea número o punto
        num = re.sub(r'[^\d.]', '', str(valor))
        try:
            return float(num)
        except:
            return 0.0

    df['salario_limpio'] = df['salario'].apply(limpiar_salario)

    # 5. Normalizar Activo (True/False)
    def normalizar_activo(valor):
        v = str(valor).lower().strip().replace('#', '')
        if v in ['true', '1', 'yes']: return True
        return False

    df['activo_bool'] = df['activo'].apply(normalizar_activo)

    return df
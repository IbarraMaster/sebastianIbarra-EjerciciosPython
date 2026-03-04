import pandas as pd
import codecs
import re
import os

def cargar_y_limpiar():
    # Ruta compatible con Windows/Linux desde la raíz del proyecto
    path = os.path.join('data', 'personas.csv')
    
    # Leemos el CSV original
    df = pd.read_csv(path)

    # --- 1. LIMPIEZA DE IDENTIDAD (ROT13 + Regex) ---
    def descifrar_y_limpiar(texto):
        if pd.isna(texto): return ""
        # Descifrar ROT13
        descifrado = codecs.decode(str(texto), 'rot_13')
        # Dejar solo letras (incluye tildes y ñ) y quitar basura
        limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', descifrado)
        return limpio.strip().title()

    df['nombre'] = df['nombre_cifrado'].apply(descifrar_y_limpiar)
    df['apellido'] = df['apellido_cifrado'].apply(descifrar_y_limpiar)

    # --- 2. LIMPIEZA DE TEXTO GENERAL (Ciudad y Profesión) ---
    def limpiar_texto(texto):
        if pd.isna(texto): return ""
        # Quitamos caracteres especiales como @, %, !, números, etc.
        limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', str(texto))
        return limpio.strip().title()

    df['ciudad'] = df['ciudad'].apply(limpiar_texto)
    df['profesion'] = df['profesion'].apply(limpiar_texto)

    # --- 3. LIMPIEZA DE SALARIO (Filtro de Outliers) ---
    def limpiar_salario(valor):
        if pd.isna(valor): return 0.0
        # Extraer solo los números (quita símbolos de moneda, puntos, comas)
        num_solo = re.sub(r'\D', '', str(valor))
        if not num_solo: return 0.0
        
        n = float(num_solo)
        
        # FILTRO DE SEGURIDAD: 
        # Si el valor supera los 100 millones, asumimos que es un error de carga 
        # (como los Unix Timestamps que vimos de 1.400 millones).
        if n > 100000000: 
            return 0.0
        return n

    df['salario_limpio'] = df['salario'].apply(limpiar_salario)

    # --- 4. NORMALIZACIÓN DE ESTADO ACTIVO (Booleanos) ---
    def limpiar_activo(valor):
        v = str(valor).lower().strip()
        # Identificamos cualquier variante de "Verdadero"
        if any(x in v for x in ['true', '1', 'yes', 'si', 'active', 'activo']): 
            return True
        return False

    df['activo_bool'] = df['activo'].apply(limpiar_activo)

    return df
import pandas as pd
import codecs
import re
import os


def cargar_y_limpiar():
    path = os.path.join('data', 'personas.csv')
    df = pd.read_csv(path)

    # ------------------------------------------------------------------ #
    # 1. NOMBRE Y APELLIDO — ROT13 + limpieza de caracteres
    # ------------------------------------------------------------------ #
    def descifrar_y_limpiar(texto):
        if pd.isna(texto):
            return ""
        descifrado = codecs.decode(str(texto), 'rot_13')
        limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', descifrado)
        return limpio.strip().title()

    df['nombre']   = df['nombre_cifrado'].apply(descifrar_y_limpiar)
    df['apellido'] = df['apellido_cifrado'].apply(descifrar_y_limpiar)

    # ------------------------------------------------------------------ #
    # 2. CIUDAD — quitar símbolos + corregir abreviaciones
    # ~4.500 registros tienen vocales eliminadas (ej: 'Bogot', 'Mdllin')
    # ------------------------------------------------------------------ #
    CIUDAD_MAP = {
        'Armni': 'Armenia',          'Bogot': 'Bogota',
        'Brrnquill': 'Barranquilla', 'Bucrmng': 'Bucaramanga',
        'Cli': 'Cali',               'Crtgn': 'Cartagena',
        'Cucut': 'Cucuta',           'Ibgu': 'Ibague',
        'Mnizls': 'Manizales',       'Mdllin': 'Medellin',
        'Montri': 'Monteria',        'Niv': 'Neiva',
        'Psto': 'Pasto',             'Prir': 'Pereira',
        'Popyn': 'Popayan',          'Snt Mrt': 'Santa Marta',
        'Sincljo': 'Sincelejo',      'Tunj': 'Tunja',
        'Vlldupr': 'Valledupar',     'Villvicncio': 'Villavicencio',
    }

    def limpiar_ciudad(texto):
        if pd.isna(texto):
            return ""
        limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', str(texto)).strip().title()
        return CIUDAD_MAP.get(limpio, limpio)

    df['ciudad'] = df['ciudad'].apply(limpiar_ciudad)

    # ------------------------------------------------------------------ #
    # 3. PROFESIÓN — quitar símbolos + corregir abreviaciones
    # ------------------------------------------------------------------ #
    PROFESION_MAP = {
        'Abogdo': 'Abogado',          'Administrdor': 'Administrador',
        'Arquitcto': 'Arquitecto',    'Chf': 'Chef',
        'Contdor': 'Contador',        'Crpintro': 'Carpintero',
        'Disndor': 'Disenador',       'Economist': 'Economista',
        'Elctricist': 'Electricista', 'Enfrmro': 'Enfermero',
        'Ingniro': 'Ingeniero',       'Mcnico': 'Mecanico',
        'Mdico': 'Medico',            'Plomro': 'Plomero',
        'Priodist': 'Periodista',     'Profsor': 'Profesor',
        'Progrmdor': 'Programador',   'Trductor': 'Traductor',
        'Vtrinrio': 'Veterinario',
    }

    def limpiar_profesion(texto):
        if pd.isna(texto):
            return ""
        limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', str(texto)).strip().title()
        return PROFESION_MAP.get(limpio, limpio)

    df['profesion'] = df['profesion'].apply(limpiar_profesion)

    # ------------------------------------------------------------------ #
    # 4. EMAIL — eliminar espacios + prefijos/sufijos de formato
    # Tipos de suciedad encontrados:
    #   - Espacios internos:  'ana @ hotmail.com'       (~45.000 registros)
    #   - Paréntesis:         '(usuario@mail.com)'      (~8.900 registros)
    #   - Ángulos HTML:       '<usuario@mail.com>'      (~8.800 registros)
    #   - Prefijo mailto:     'mailto:usuario@mail.com' (~9.000 registros)
    # ------------------------------------------------------------------ #
    def limpiar_email(valor):
        if pd.isna(valor):
            return ""
        s = str(valor).replace(' ', '').lower()
        s = re.sub(r'^mailto:', '', s)       # quitar prefijo mailto:
        s = re.sub(r'^[\(<]|[\)>]$', '', s) # quitar envolturas ( ) < >
        return s

    df['email_limpio'] = df['email'].apply(limpiar_email)

    # ------------------------------------------------------------------ #
    # 5. SALARIO — corregir l→1 y O→0 antes de extraer dígitos
    # Umbral máximo: 15.000.000 (gap comprobado: no existen valores válidos
    # entre 15M y 100M; los que superan 15M son timestamps / datos corruptos)
    # ------------------------------------------------------------------ #
    def limpiar_salario(valor):
        if pd.isna(valor):
            return None
        s = str(valor)
        # Corregir confusiones tipográficas: 'l' (ele) → '1', 'O' (letra O) → '0'
        s = s.replace('l', '1').replace('O', '0')
        num_solo = re.sub(r'\D', '', s)
        if not num_solo:
            return None
        n = float(num_solo)
        if n > 15_000_000:
            return None
        return n

    df['salario_limpio'] = df['salario'].apply(limpiar_salario)

    # ------------------------------------------------------------------ #
    # 6. ACTIVO — normalizar todas las variantes a booleano
    # Limpia símbolos sueltos (@False, #True, False%) antes de comparar
    # ------------------------------------------------------------------ #
    def limpiar_activo(valor):
        v = re.sub(r'[^a-zA-Z0-9]', '', str(valor)).lower().strip()
        return v in {'true', '1', 'yes', 'si', 'active', 'activo'}

    df['activo_bool'] = df['activo'].apply(limpiar_activo)

    # ------------------------------------------------------------------ #
    # 7. FECHA DE NACIMIENTO — normalizar a YYYY-MM-DD
    # Soporta: YYYY-MM-DD, YYYY.MM.DD, YYYY/MM/DD,
    #          espacios internos (19 92-04-21), chars raros (@, ~, %, #)
    # Estrategia: extraer solo los 8 dígitos y recomponer.
    # ------------------------------------------------------------------ #
    def limpiar_fecha(valor):
        if pd.isna(valor):
            return None
        solo_digitos = re.sub(r'\D', '', str(valor))
        if len(solo_digitos) == 8:
            return f"{solo_digitos[:4]}-{solo_digitos[4:6]}-{solo_digitos[6:8]}"
        return None

    df['fecha_limpia'] = pd.to_datetime(
        df['fecha_nacimiento'].apply(limpiar_fecha), errors='coerce'
    )

    return df
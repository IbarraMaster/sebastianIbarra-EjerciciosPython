# Taller de Procesamiento de Datos con Python - Universidad CESMAG

Este repositorio contiene la solución al taller de 30 ejercicios de procesamiento y limpieza de datos sobre un dataset de 300,000 registros de ciudadanos.

## 🛠️ Tecnologías Utilizadas

* **Python 3.12+**
* **Pandas:** Para la manipulación y análisis de datos.
* **UV:** Gestor de paquetes y entornos de última generación (Astral).
* **Git:** Control de versiones.

## 🚀 Guía de Configuración y Ejecución

Para garantizar que el proyecto funcione correctamente y de forma aislada, se recomienda el uso de **uv**.

### 1. Clonar el repositorio

```bash
git clone https://github.com/IbarraMaster/sebastianIbarra-EjerciciosPython.git
cd sebastianIbarra-EjerciciosPython
```

### 2. Configurar el entorno virtual

Sincroniza las dependencias y crea el entorno virtual automáticamente con:

```bash
uv sync
```

### 3. Ejecutar los ejercicios

No es necesario activar el entorno manualmente si usas `uv run`. Por ejemplo, para ver el resultado del ejercicio 17:

```bash
uv run soluciones/xx.py #en 'xx' reemplazar por el numero de ejercicio que se quiera ejecutar.
```

## 🧹 Lógica de Limpieza (Módulo Maestro)

La inteligencia del proyecto reside en `soluciones/utils.py`, donde se centralizaron los procesos de limpieza para asegurar la integridad de los resultados:

* **Nombres y Apellidos:** Descifrado mediante ROT13 y normalización a Title Case.
* **Ciudades y Profesiones:** Limpieza de caracteres especiales y corrección de ~20 variantes ortográficas mediante diccionarios de mapeo (ej. `Mdllin` → `Medellin`).
* **Emails:** Eliminación de espacios internos y corrección de formatos inválidos como `(usuario@mail.com)`, `<usuario@mail.com>` y `mailto:usuario@mail.com`.
* **Salarios:** Corrección de errores tipográficos (`l` → `1`, `O` → `0`) y filtrado de datos corruptos (umbral de $15,000,000 verificado por gap estadístico en el dataset).
* **Fechas:** Extracción de dígitos y estandarización al formato ISO 8601 (`YYYY-MM-DD`), soportando variantes con `.`, `/`, espacios internos y caracteres especiales.
* **Booleano de Actividad:** Normalización de múltiples variantes (`1`, `si`, `active`, `true`, `yes`) a valores booleanos reales.

## Ejercicios y Soluciones

A continuación se listan los 30 ejercicios. **Debe escribir el valor exacto de la respuesta** en la columna "Solución".

| # | Ejercicio | Solución |
|---|-----------|----------|
| 01 | ¿Cuántas filas tienen el campo `id` con caracteres no numéricos? | `83648` |
| 02 | ¿Cuántas veces aparece el nombre "Maria" en el dataset? | `4160` |
| 03 | ¿Cuántas veces aparece el nombre "Juan" en el dataset? | `3986` |
| 04 | ¿Cuál es el nombre más frecuente y cuántas veces aparece? | `Gonzalo 4221` |
| 05 | ¿Cuál es el apellido más frecuente y cuántas veces aparece? | `Reyes 7490 ` |
| 06 | ¿Cuántos registros tienen la ciudad "Bogota" después de limpiar? | `14969` |
| 07 | ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar? | `15193` |
| 08 | ¿Cuántas ciudades únicas existen después de normalizar? | `20` |
| 09 | ¿Cuántos registros tienen la profesión "Ingeniero" después de limpiar? | `12083` |
| 10 | ¿Cuántos registros tienen la profesión "Programador" después de limpiar? | `12062` |
| 11 | ¿Cuántas profesiones únicas existen después de normalizar? | `25` |
| 12 | ¿Cuántos registros tienen el campo `email` con espacios adicionales? | `45447` |
| 13 | ¿Cuántos registros tienen el campo `salario` con caracteres no numéricos? | `85266` |
| 14 | ¿Cuál es el salario promedio después de limpiar? | `8.004.542` |
| 15 | ¿Cuál es el salario máximo después de limpiar? | `14.999.995` |
| 16 | ¿Cuál es el salario mínimo después de limpiar? | `1.000.032` |
| 17 | ¿Cuántos registros tienen `activo` como verdadero después de normalizar? | `149863` |
| 18 | ¿Cuántos registros tienen `activo` como falso después de normalizar? | `150137` |
| 19 | ¿Cuántos registros tienen fecha de nacimiento con formato diferente a YYYY-MM-DD? | `89823` |
| 20 | ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive)? | `53404` |
| 21 | ¿Cuántas personas nacieron antes de 1960? | `66577` |
| 22 | ¿Cuántas personas tienen más de 50 años (fecha actual: 2026-02-26)? | `144846` |
| 23 | ¿Cuántos registros tienen nombre "Carlos" y viven en "Cali"? | `187` |
| 24 | ¿Cuántos registros tienen nombre "Ana" y son "Medico"? | `172` |
| 25 | ¿Cuántos registros tienen profesión "Abogado" y salario > 10,000,000? | `4300` |
| 26 | ¿Cuántos registros tienen ciudad "Barranquilla", activos y nacidos después de 1980? | `3241` |
| 27 | ¿Cuál es la ciudad con más "Ingenieros"? | `Popayan` |
| 28 | ¿Cuál es la profesión con el salario promedio más alto? | `Administrador` |
| 29 | ¿Cuántos registros tienen email con dominio "gmail.com"? | `60000` |
| 30 | ¿Cuántos registros tienen nombre "Jose" y apellido "Garcia"? | `96` |

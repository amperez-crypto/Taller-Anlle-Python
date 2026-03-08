# Taller Python - Manejo y Limpieza de Datos
### Infraestructura para Grandes Volúmenes de Datos

---

## Herramientas utilizadas
- **Python** con librerías `pandas`, `re`, `codecs`, `sqlite3`
- **Visual Studio Code** como entorno de desarrollo
- **SQLite** para verificación de datos limpios

---

## Proceso de solución

### 1. Exploración inicial
Se cargó el dataset `data/personas.csv` (300,000 filas) y se identificaron los tipos de datos sucios en cada columna.

### 2. Limpieza de datos (`limpieza.py`)
Se creó un archivo central de limpieza que procesa todas las columnas:

- **nombre / apellido**: Se quitaron caracteres especiales y se descifraron con ROT13
- **ciudad / profesion**: Se eliminaron tildes, caracteres especiales y se normalizó a mayúsculas. Se aplicó un mapeo para corregir profesiones con vocales faltantes (`PROFSOR → PROFESOR`, `MCNICO → MECANICO`, etc.)
- **salario**: Se reemplazaron letras similares a números (`l→1`, `O→0`), se eliminó el prefijo `aprox.` y se normalizó la coma decimal. Salarios menores a 1,000 se descartaron como inválidos.
- **fecha_nacimiento**: Se parseó con `pd.to_datetime(errors='coerce')`
- **activo**: Se normalizaron valores como `true/false/si/no/1/0/verdadero/falso`
- **email**: Se eliminaron espacios con `str.strip()`

### 3. Verificación
Los datos limpios se exportaron a `personas_limpias.db` (SQLite) para verificar resultados con SQL antes de escribir cada solución en Python.

### 4. Soluciones
Cada ejercicio está en `soluciones/XX.py` y lee desde el CSV original o la base de datos limpia según lo requiera el ejercicio.

---

## Soluciones

| # | Ejercicio | Solución |
|---|-----------|----------|
| 01 | ¿Cuántas filas tienen el campo id con caracteres no numéricos? | 83648 |
| 02 | ¿Cuántas veces aparece el nombre "Maria"? | 4160 |
| 03 | ¿Cuántas veces aparece el nombre "Juan"? | 3986 |
| 04 | ¿Cuál es el nombre más frecuente y cuántas veces aparece? | Gonzalo, 4221 |
| 05 | ¿Cuál es el apellido más frecuente y cuántas veces aparece? | Rivera, 7490 |
| 06 | ¿Cuántos registros tienen la ciudad "Bogota" después de limpiar? | 14739 |
| 07 | ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar? | 14989 |
| 08 | ¿Cuántas ciudades únicas existen después de normalizar? | 40 |
| 09 | ¿Cuántos registros tienen la profesión "Ingeniero" después de limpiar? | 11899 |
| 10 | ¿Cuántos registros tienen la profesión "Programador" después de limpiar? | 11875 |
| 11 | ¿Cuántas profesiones únicas existen después de normalizar? | 44 |
| 12 | ¿Cuántos registros tienen el campo email con espacios adicionales? | 27075 |
| 13 | ¿Cuántos registros tienen el campo salario con caracteres no numéricos? | 85266 |
| 14 | ¿Cuál es el salario promedio después de limpiar? | 8007002.59 |
| 15 | ¿Cuál es el salario máximo después de limpiar? | 14999995.0 |
| 16 | ¿Cuál es el salario mínimo después de limpiar? | 1000032.0 |
| 17 | ¿Cuántos registros tienen activo como verdadero después de normalizar? | 139582 |
| 18 | ¿Cuántos registros tienen activo como falso después de normalizar? | 138878 |
| 19 | ¿Cuántos registros tienen fecha de nacimiento con formato diferente a YYYY-MM-DD? | 89823 |
| 20 | ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive)? | 37518 |
| 21 | ¿Cuántas personas nacieron antes de 1960? | 46713 |
| 22 | ¿Cuántas personas tienen más de 50 años (fecha actual: 2026-02-26)? | 101536 |
| 23 | ¿Cuántos registros tienen nombre "Carlos" y viven en "Cali"? | 186 |
| 24 | ¿Cuántos registros tienen nombre "Ana" y son "Medico"? | 170 |
| 25 | ¿Cuántos registros tienen profesión "Abogado" y salario > 10,000,000? | 4269 |
| 26 | ¿Cuántos registros tienen ciudad "Barranquilla", activos y nacidos después de 1980? | 2082 |
| 27 | ¿Cuál es la ciudad con más "Ingenieros"? | POPAYAN, 618 |
| 28 | ¿Cuál es la profesión con el salario promedio más alto? | ADMINISTRADOR |
| 29 | ¿Cuántos registros tienen email con dominio "gmail.com"? | 49273 |
| 30 | ¿Cuántos registros tienen nombre "Jose" y apellido "Garcia"? | 96 |

---

## Estructura del repositorio

```
├── soluciones/
│   ├── 01.py
│   ├── 02.py
│   └── ... (30 archivos)
├── data/
│   └── personas.csv
├── limpieza.py
├── README.md
└── README_SOLUCIONES.md
```

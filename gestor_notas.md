# Gestor de Notas de Alumnos

El programa permitirá gestionar las notas de múltiples alumnos, incorporando funcionalidades de entrada, validación, cálculo de la nota final y generación de informes. A continuación, se detallan las opciones disponibles:

## 1. Menú Principal

El programa presentará un menú con las siguientes opciones:

1. **Añadir alumno**
2. **Introducir notas**
3. **Generar informe**
5. **Salir**

---

## 2. Funcionalidades del Programa

### 1. Añadir alumno (NIF/NIE y Nombre)

- Se solicitará un **nombre** y un **NIF o NIE** válido:
  - El nombre no puede estar vacío.
  - Un **DNI** tiene 8 dígitos y una letra de control. Ejemplo: `12345678A`
  - Un **NIE** comienza con `X`, `Y` o `Z`, seguido de 7 dígitos y una letra de control. Ejemplo: `X1234567A`
- **Validaciones:**
  - Se verificará que el formato sea correcto (posiciones de letras y números) y que la letra de control sea válida según el algoritmo de verificación del NIF/NIE.
  - Se permitirá introducir el NIF/NIE con letras en mayúsculas o minúsculas.
  - Si el formato es incorrecto, **se volverá a pedir hasta que sea válido o se introduzca 5 veces erroneamente**.
  - **No se podrá introducir un NIF/NIE ya existente.**
- Una vez introducido, el alumno se registrará en el sistema sin notas asignadas inicialmente.

### 2. Introducir o modificar notas

- Se pedirá el NIF del alumno al que se quieren introducir las notas.
- Se solicitarán las tres notas (`P1`, `P2`, `P3`) en una única línea, separadas por espacios.
- **Validaciones:**
  - Cada nota será un número con 2 decimales, entre **0,00 y 10,00**.
  - Se verificarán que se hayan introducido exactamente 3 valores.
  - Si algún valor es incorrecto o está fuera de rango, se pedirá que se introduzcan nuevamente, **indicando cuál es el valor erroneo**.

### 3. Generar informe

- La nota final se calculará con la siguiente media ponderada:

$$ \text{Media Ponderada} = (P1 \times 0.3) + (P2 \times 0.4) + (P3 \times 0.3) $$

- **Condiciones especiales:**

  - Para aprobar, es necesario haber obtenido al menos **3,0 puntos** en `P2` y `P3`.
  - Si la media ponderada es menor que 4, la nota final será la media ponderada.
  - Si la media ponderada es mayor o igual que 4 pero `P2` o `P3` es inferior a 3, la nota final se limitará a **4,00**.
  - Si la nota final es **mayor o igual que 5,00**, el resultado será **APROBADO**, en caso contrario será **SUSPENSO**.

El informe incluirá los siguientes datos:

- **Nombre del alumno**.
- **NIF/NIE** del alumno.
- **Notas** de las pruebas `P1`, `P2` y `P3`.
- **Media ponderada calculada**.
- **Nota final aplicada**.
- **Resultado**: `APROBADO` o `SUSPENSO`.

**Formato de salida:**

- Todas las notas se mostrarán con 2 decimales, con los decimales separados por coma.
- Ejemplo de salida:
  ```
  Nombre: Juan Pérez
  NIF/NIE: X1234567A
  P1: 7,50 | P2: 2,80 | P3: 5,00
  Media Ponderada: 5,08
  Nota Final: 4,00
  Resultado: SUSPENSO
  ```

### 5. Salir

- Se mostrará un mensaje de despedida y finalizará la ejecución del programa.

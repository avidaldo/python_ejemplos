"""
Evaluación de Expresiones Booleanas en Python

Este script explica cómo Python evalúa expresiones booleanas y demuestra
el error común de confundir:
    opcion == '1' or 'a'  # INCORRECTO
    opcion == '1' or opcion == 'a'  # CORRECTO
"""

# ============================================================================
# PARTE 1: Valores Booleanos en Python
# ============================================================================

# En Python, los siguientes valores se evalúan como False:
# - False
# - None
# - 0 (entero cero)
# - 0.0 (flotante cero)
# - '' (cadena vacía)
# - [] (lista vacía)
# - {} (diccionario vacío)
# - set() (conjunto vacío)
# - () (tupla vacía)

# Todos los demás valores se evalúan como True

print("=== Valores que se evalúan como False ===")
print(f"bool(False): {bool(False)}")
print(f"bool(None): {bool(None)}")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool({}): {bool({})}")
print(f"bool(()): {bool(())}")

print("\n=== Valores que se evalúan como True ===")
print(f"bool(True): {bool(True)}")
print(f"bool(1): {bool(1)}")
print(f"bool('a'): {bool('a')}")  # Cualquier string no vacío
print(f"bool([0]): {bool([0])}")  # Cualquier lista no vacía
print(f"bool({'key': 'value'}): {bool({'key': 'value'})}")

# ============================================================================
# PARTE 2: El ERROR COMÚN - Evaluación incorrecta de expresiones booleanas
# ============================================================================

# Vamos a analizar paso a paso por qué:
#    opcion == '1' or 'a'  
# NO es lo mismo que:
#    opcion == '1' or opcion == 'a'

print("\n=== DEMOSTRACIÓN DEL ERROR COMÚN ===")

# Definimos algunas variables para probar
opcion1 = '1'
opcion2 = 'a'
opcion3 = 'b'

# Forma INCORRECTA:
print("\n== Evaluación INCORRECTA: opcion == '1' or 'a' ==")

# Caso 1: cuando opcion = '1'
resultado1 = opcion1 == '1' or 'a'
print(f"Con opcion = '{opcion1}': (opcion == '1' or 'a') = {resultado1}")
# Explicación: 
# 1. opcion1 == '1' evalúa a True
# 2. True or 'a' siempre es True (porque el primer operando ya es True)
# 3. Por tanto, el resultado es True

# Caso 2: cuando opcion = 'a'
resultado2 = opcion2 == '1' or 'a'
print(f"Con opcion = '{opcion2}': (opcion == '1' or 'a') = {resultado2}")
# Explicación:
# 1. opcion2 == '1' evalúa a False
# 2. False or 'a' evalúa el segundo operando
# 3. 'a' NO es un booleano, pero se evalúa como True porque es una cadena no vacía
# 4. Por tanto, el resultado es 'a' (¡no True!)

# Caso 3: cuando opcion = 'b'
resultado3 = opcion3 == '1' or 'a'
print(f"Con opcion = '{opcion3}': (opcion == '1' or 'a') = {resultado3}")
# Explicación:
# 1. opcion3 == '1' evalúa a False
# 2. False or 'a' evalúa el segundo operando
# 3. 'a' se evalúa como True porque es una cadena no vacía
# 4. Por tanto, el resultado es 'a' (¡no True!)

# ============================================================================
# PARTE 3: La Forma CORRECTA
# ============================================================================

print("\n== Evaluación CORRECTA: opcion == '1' or opcion == 'a' ==")

# Caso 1: cuando opcion = '1'
resultado4 = opcion1 == '1' or opcion1 == 'a'
print(f"Con opcion = '{opcion1}': (opcion == '1' or opcion == 'a') = {resultado4}")
# Explicación:
# 1. opcion1 == '1' evalúa a True
# 2. True or cualquier_cosa no evalúa el segundo operando (cortocircuito)
# 3. El resultado es True

# Caso 2: cuando opcion = 'a'
resultado5 = opcion2 == '1' or opcion2 == 'a'
print(f"Con opcion = '{opcion2}': (opcion == '1' or opcion == 'a') = {resultado5}")
# Explicación:
# 1. opcion2 == '1' evalúa a False
# 2. False or opcion2 == 'a' evalúa el segundo operando
# 3. opcion2 == 'a' evalúa a True
# 4. El resultado es True

# Caso 3: cuando opcion = 'b'
resultado6 = opcion3 == '1' or opcion3 == 'a'
print(f"Con opcion = '{opcion3}': (opcion == '1' or opcion == 'a') = {resultado6}")
# Explicación:
# 1. opcion3 == '1' evalúa a False
# 2. False or opcion3 == 'a' evalúa el segundo operando
# 3. opcion3 == 'a' evalúa a False
# 4. El resultado es False

# ============================================================================
# PARTE 4: Cortocircuito en expresiones booleanas
# ============================================================================

print("\n=== CORTOCIRCUITO EN OPERACIONES BOOLEANAS ===")

# El operador OR utiliza cortocircuito (short-circuit)
# Si el primer operando es True, el segundo no se evalúa
print("\n== Cortocircuito con OR ==")
a = True
print(f"True or print('Esto no se muestra') = {a or print('Esto no se muestra')}")

b = False
print(f"False or 'Se evalúa esto' = {b or 'Se evalúa esto'}")

# El operador AND también utiliza cortocircuito
# Si el primer operando es False, el segundo no se evalúa
print("\n== Cortocircuito con AND ==")
c = False
print(f"False and print('Esto no se muestra') = {c and print('Esto no se muestra')}")

d = True
print(f"True and 'Se evalúa esto' = {d and 'Se evalúa esto'}")

# ============================================================================
# PARTE 5: Solución correcta para verificar múltiples opciones
# ============================================================================

print("\n=== SOLUCIONES CORRECTAS PARA COMPROBAR MÚLTIPLES VALORES ===")

# Opción 1: Comparaciones explícitas (la más clara)
def verificar_opcion1(opcion):
    return opcion == '1' or opcion == 'a'

# Opción 2: Usar el operador "in" con una colección
def verificar_opcion2(opcion):
    return opcion in ['1', 'a']

# Probemos ambas opciones
valores_a_probar = ['1', 'a', 'b', '']

print("\nResultados con diferentes métodos:")
for valor in valores_a_probar:
    print(f"Valor: '{valor}'")
    print(f"  - Comparaciones explícitas: {verificar_opcion1(valor)}")
    print(f"  - Operador 'in': {verificar_opcion2(valor)}")

# ============================================================================
# CONCLUSIÓN
# ============================================================================
"""
PUNTOS CLAVE A RECORDAR:

1. La expresión "opcion == '1' or 'a'" NO equivale a "opcion == '1' or opcion == 'a'"
   - La primera evalúa si opcion es igual a '1' O si 'a' es un valor considerado True
   - La segunda evalúa si opcion es igual a '1' O si opcion es igual a 'a'

2. El operador OR devuelve:
   - El primer operando si éste es True (o se evalúa como True)
   - El segundo operando en caso contrario

3. Las mejores formas de comprobar si una variable está dentro de un conjunto de valores son:
   - Comparaciones explícitas: opcion == '1' or opcion == 'a'
   - Operador 'in': opcion in ['1', 'a']

4. Recuerda que en Python cualquier string no vacío se evalúa como True

5. Los operadores lógicos AND y OR utilizan evaluación de cortocircuito (short-circuit),
   lo que significa que pueden no evaluar todos los operandos.
"""

"""
Diferentes implementaciones del cálculo de potencia usando bucles.
Cada función implementa el mismo comportamiento: calcula base^exponente sin usar el operador **.
"""

# ---------------------------- SIN USAR abs() ----------------------------

def potencia_simple(base, exponente):
    """
    Versión más básica y directa.
    Separa los casos positivo y negativo desde el principio.
    Ventaja: Muy fácil de entender, lógica directa
    Desventaja: Duplica algo de código
    """
    resultado = 1
    if exponente >= 0:
        for _ in range(exponente):
            resultado *= base
    else:
        for _ in range(-exponente):
            resultado *= 1/base
    return resultado


def potencia_signo(base, exponente):
    """
    Similar a la versión simple pero usando un multiplicador según el signo.
    Ventaja: Evita duplicar el bucle
    Desventaja: El concepto de multiplicador puede ser más abstracto
    """
    resultado = 1
    multiplicador = base if exponente >= 0 else 1/base
    for _ in range(exponente if exponente >= 0 else -exponente):
        resultado *= multiplicador
    return resultado


def potencia_contador(base, exponente):
    """
    Usa un contador que sube o baja hasta llegar a cero.
    Ventaja: Más intuitiva para algunos, similar a cómo lo haríamos manualmente
    Desventaja: Más compleja y menos eficiente
    """
    resultado = 1
    contador = exponente
    while contador != 0:
        if contador > 0:
            resultado *= base
            contador -= 1
        else:
            resultado *= 1/base
            contador += 1
    return resultado


def potencia_ajuste_posterior(base, exponente):
    """
    Calcula primero como si fuera positivo y luego ajusta.
    Similar al método original del ejercicio.
    Ventaja: Separa claramente el cálculo del ajuste
    Desventaja: Hace dos pasos cuando podría hacerse en uno
    """
    potencia_pos = -exponente if exponente < 0 else exponente
    resultado = 1
    for _ in range(potencia_pos):
        resultado *= base
    if exponente < 0:
        resultado = 1 / resultado
    return resultado


# ---------------------------- USANDO abs() ----------------------------

def potencia_abs_simple(base, exponente):
    """
    La versión más simple usando abs().
    Ventaja: Muy concisa y clara
    Desventaja: Usa abs() que podría no estar permitido
    """
    resultado = 1
    for _ in range(abs(exponente)):
        resultado *= base
    return 1/resultado if exponente < 0 else resultado


def potencia_abs_multiplicador(base, exponente):
    """
    Usa abs() con un multiplicador directo.
    Ventaja: Evita el if final
    Desventaja: La expresión del multiplicador es más compleja
    """
    resultado = 1
    for _ in range(abs(exponente)):
        resultado = resultado * base if exponente > 0 else resultado * (1/base)
    return resultado


def potencia_abs_lista(base, exponente):
    """
    Usa una lista de multiplicadores (versión más pythónica).
    Ventaja: Muy pythónica, usa características del lenguaje
    Desventaja: Menos eficiente en memoria, más abstracta
    """
    resultado = 1
    multiplicadores = [base] * abs(exponente)
    for n in multiplicadores:
        resultado *= n
    return 1/resultado if exponente < 0 else resultado


# Función para probar todas las implementaciones
def probar_implementaciones():
    """
    Prueba todas las implementaciones con varios casos de prueba
    """
    casos_prueba = [
        (2, 3),    # positivo ^ positivo
        (2, -3),   # positivo ^ negativo
        (-2, 3),   # negativo ^ positivo
        (-2, -3),  # negativo ^ negativo
        (2, 0),    # cualquier número ^ 0
        (0, 3),    # 0 ^ positivo
    ]
    
    funciones = [
        potencia_simple,
        potencia_signo,
        potencia_contador,
        potencia_ajuste_posterior,
        potencia_abs_simple,
        potencia_abs_multiplicador,
        potencia_abs_lista
    ]
    
    for base, exp in casos_prueba:
        print(f"\nProbando {base}^{exp}:")
        resultado_python = base ** exp  # resultado correcto usando Python
        print(f"Resultado Python: {resultado_python}")
        
        for func in funciones:
            try:
                resultado = func(base, exp)
                print(f"{func.__name__}: {resultado}")
                assert abs(resultado - resultado_python) < 1e-10, "Resultado incorrecto"
            except Exception as e:
                print(f"{func.__name__}: Error - {str(e)}")


if __name__ == "__main__":
    probar_implementaciones() 
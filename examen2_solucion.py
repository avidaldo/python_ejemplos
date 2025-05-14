lista_estudiantes = [
    ['Pedro', '31254321S', 4.3, 5.2, 7.3], 
    ['Ana', '45321234G', 5.0, 9.9, 8.5], 
    ['Victoria', '43212321D', 6.0, 8.5, 10], 
    ['Fernando', '32789896S', 7.0, 10, 9.5],
]


def calcula_nota_final(p1, p2, p3):
    media_ponderada = .3*p1 + .4*p2 + .3*p3
    if media_ponderada >= 4 and (p2 < 3 or p3 < 3):
        nota_final = 4
    else:
        nota_final = media_ponderada
    return round(nota_final, 2)


def fila_estudiante(lista_estudiantes, dni):
    for fila in lista_estudiantes:
        if fila[1] == dni:
            return fila
    return None


def nota_global_estudiante(lista_estudiantes, dni):
    fila = fila_estudiante(lista_estudiantes, dni)
    if fila is None:
        return None
    return calcula_nota_final(fila[2], fila[3], fila[4])


def lista_aprobados(lista_estudiantes):
    aprobados = []
    for fila in lista_estudiantes:
        if calcula_nota_final(fila[2], fila[3], fila[4]) >= 5:
            aprobados.append(fila)
    return aprobados


def modificar_nota(lista_estudiantes, dni, num_examen, nueva_nota): 
    if num_examen not in (1, 2, 3):
        raise ValueError("El número de examen debe ser 1, 2 o 3")
    for fila in lista_estudiantes:
        if fila[1] == dni:
            fila[2 + num_examen] = nueva_nota
            return True
    return False

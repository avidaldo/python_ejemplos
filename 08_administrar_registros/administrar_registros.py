def leerRegistros(nombre):
    registros=[]
    fichero=open(nombre,'r',encoding='utf-8')
    for linea in fichero:
        nuevoRegistro=[]
        c=linea[:-1].split(';') # eliminamos el retorno de carro al final y dividimos la línea usando ; como separador
        nuevoRegistro.append(c[0])
        nuevoRegistro.append(int(c[1])) # lo convertimos a entero
        nuevoRegistro.append(float(c[2].replace(',','.'))) # sustituimos , por . y convertimos a flotante
        nuevoRegistro.append(c[3])
        nuevoRegistro.append(c[4]) 
        registros.append(nuevoRegistro)
    fichero.close()
    return(registros)

def imprimirRegistros(registros):
    plantilla='Nombre: {}  Edad: {}  Salario: {} €  NIF: {}   Teléfono: {}'
    for r in registros:
        print(plantilla.format(r[0],r[1],round(r[2],2),r[3],r[4]))

def añadirRegistro(registros):
    nuevoRegistro=[]
    nuevoRegistro.append(input('Nombre: '))
    nuevoRegistro.append(int(input('Edad: ')))
    nuevoRegistro.append(float(input('Salario: ')))
    nuevoRegistro.append(input('NIF: '))
    nuevoRegistro.append(input('Teléfono: '))
    registros.append(nuevoRegistro)

def borrarRegistro(registros, posicion):
    registros.pop(posicion-1)
    
def guardarRegistros(nombre,registros):
    plantilla='{};{};{};{};{}\n' # formato de cada línea
    fichero=open(nombre,'w',encoding='utf-8') # w hará que sobrescribamos el fichero existente 
    for r in registros:
        salario=str(r[2]).replace('.',',') # Lo almacenamos con el formato decimal de España
        fichero.write(plantilla.format(r[0],r[1],salario,r[3],r[4]))
    fichero.close()    

menu='''Selecciona una de las siguientes opciones:
A: Leer
B: Imprimir
C: Añadir
D: Borrar
E: Guardar
Q: Salir
'''
registros=[]
nombreFichero='./registros.csv'
while True:
    opcion=input(menu).upper()
    if opcion=='A':
        registros=leerRegistros(nombreFichero) # Sobrescribirá el array en memoria
    elif opcion=='B':
        imprimirRegistros(registros)
    elif opcion=='C':
        añadirRegistro(registros) # al ser una lista se pasa como referencia, y será modificado en el interior de la función
    elif opcion=='D':
        posicion=int(input('Qué registro quiere borrar (comienzan en la posición 1)?'))
        borrarRegistro(registros,posicion)
    elif opcion=='E':
        guardarRegistros(nombreFichero,registros)
    elif opcion=='Q':
        break
    else:
        print('Opción inválida')
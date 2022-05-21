#Busqueda hash, TÉCNICA DE RESOLUCIÓN COLISIONES: ENCADENAMIENTO / HASHING ABIERTO

def conviertoCadena(cad):
    salida = ""
    for i in cad:
        salida += str(ord(i))
    return int(salida)
#cad = cadena
#m = tamaño tabla
def funcion_hash(cad,m):
    i = conviertoCadena(cad)
    return int(m*(i*0.0000002%1))


def agregar (cad,ht,m):
    resp = funcion_hash(cad,m)
    ht[resp].append(cad)

def buscar(cad,ht,m):
    h = funcion_hash(cad,m)
    for i in ht[h]:
        if i == cad:
            return True
    return False

m = 19#Tamaño tabla
tabla_hash = [[]for i in range(m)]

agregar("Nacho",tabla_hash,m)
agregar("Flexo",tabla_hash,m)
agregar("Boligrafo",tabla_hash,m)
agregar("teclado",tabla_hash,m)
agregar("Lapiz",tabla_hash,m)
agregar("Rueda",tabla_hash,m)


print(tabla_hash)
print(buscar("Nacho",tabla_hash,m))

print(buscar("Libro",tabla_hash,m))
#Jossian Abimelec García Quijano

def sumarAcumulado(lista):
    nuevaLista=[]
    i=0
    for dato in lista:
        i += dato
        nuevaLista.append(i)
    return nuevaLista

    return nuevaLista


def recortarLista(lista):
    nuevaLista=[]
    for k in range(1,len(lista)-1):

        nuevaLista.append(lista[k])
    return nuevaLista




def estanOrdenador(lista):
    for k in range(0, len(lista) - 1):
        if lista[k] > lista[k + 1]:
            return False
    return True


def hayDuplicados(lista):
    for dato in lista:
        vecesDat = lista.count(dato)
        if vecesDat > 1:
            return True
        else:
            return False




def borrarDuplicados(lista):
    for dato in lista:
        veces = lista.count(dato)
        if veces > 1:
            lista.remove(dato)
            return lista
        else:
            return lista


def main():
    lista=[1,2,3,4,5]
    print("La lista",lista," regresa la lista acumulada ",sumarAcumulado(lista))
    print("La lista original", lista," regresa", recortarLista(lista))
    print(estanOrdenador(lista))
    print(hayDuplicados(lista))
    print("La lista ",lista,"regresa ",borrarDuplicados(lista))
main()
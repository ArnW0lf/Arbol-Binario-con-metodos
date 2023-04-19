'''
Nombre: Arnulfo Velasquez Paz
Registro:220030383
Fecha: 12/04/2023
'''

from Nodo import Nodo
from Arbol import ArbolBinario


def main():
    arbol = ArbolBinario()
    arbol.InsertarNodo(5)
    arbol.InsertarNodo(3)
    arbol.InsertarNodo(8)
    arbol.InsertarNodo(1)

    print(arbol.EsVacio())  # False

    print(arbol.EsHoja(arbol.raiz.left.left))  # True
    print(arbol.EsHoja(arbol.raiz.right))  # False

    print(arbol.BuscarX(8))  # True
    print(arbol.BuscarX(2))  # False

    print("Elementos mediante el metodo InOrden: ")
    arbol.InOrden(arbol.raiz)

    print("Elementos mediante el metodo PostOrden: ")
    arbol.PostOrden(arbol.raiz)


if __name__ == '__main__':
    main()

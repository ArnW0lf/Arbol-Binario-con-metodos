'''
Nombre: Arnulfo Velasquez Paz
Registro:220030383
Fecha: 12/04/2023
'''

from Nodo import Nodo

class ArbolBinario:
    def __init__(self):
        """
    Clase para crear un árbol binario.

    Atributos:
        root (Node): raíz del árbol.
    """
        self.raiz = None
    
    def InsertarNodo(self, valor):
        """
        Inserta un nuevo nodo en el árbol.

        Args:
            valor (Any): datos a almacenar en el nuevo nodo.
        """
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            actual = self.raiz
            while actual is not None:
                padre = actual
                if valor < actual.valor:
                    actual = actual.left
                else:
                    actual = actual.right
            if valor < padre.valor:
                padre.left = nuevo_nodo
            else:
                padre.right = nuevo_nodo
    
    def EsVacio(self):
        """
        verifica si el arbol esta vacio o no
        Args:
            no recive argumentos, simplemete verifica si a la raiz se le a asigndo un valor
    """    
        return self.raiz is None
    
    def EsHoja(self, nodo):
        """
        verifica si un nodo es hoja, para ello verifica si un nodo tiene hijos
        Args:
            recive como argumento el nodo
        Returns:
            bool: si el nodo tienes hijos derecho o izquierdo
    """
        return nodo is not None and nodo.left is None and nodo.right is None
    
    def BuscarX(self, valor):
        """
        Busca un nodo con datos específicos en el árbol.

        Args:
            value (Any): datos a buscar.

        Returns:
            bool: True si el nodo se encuentra en el árbol, False en caso contrario.
        """
        actual = self.raiz
        while actual is not None and actual.valor != valor:
            if valor < actual.valor:
                actual = actual.left
            else:
                actual = actual.right
        return actual is not None
    
    def InOrden(self, nodo):
        """
        Recorre los nodos del árbol en orden ascendente

        Args:
            recive como argumento la raiz del arbol

        Returns:
            devuelve una lista con los valores de los nodos en ese orden
    """
        if nodo is not None:
            self.InOrden(nodo.left)
            print(nodo.valor)
            self.InOrden(nodo.right)
    
    def PostOrden(self, nodo):
        """
        se encarga de recorrer los nodos del árbol en postorden

        Args:
            recibe como argumento un objeto de la clase "Nodo" que se desea comenzar a recorrer (por lo general se pasa la raíz del árbol
            
        Returns:
            devuelve una lista con los valores de los nodos en ese orden
    """
        if nodo is not None:
            self.PostOrden(nodo.left)
            self.PostOrden(nodo.right)
            print(nodo.valor)

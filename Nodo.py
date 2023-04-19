class Nodo:
    def __init__(self, valor):
        """
    Clase para crear un nodo de un árbol.

    Atributos:
        left (Node): nodo hijo izquierdo.
        right (Node): nodo hijo derecho.
        valor (Any): datos almacenados en el nodo.
    """

        self.left = None
        self.right = None
        self.valor = valor
    
    def get_valor(self):
        """
        Obtiene los datos almacenados en el nodo.

        Returns:
            Any: datos almacenados en el nodo.
        """
        return self.valor
    
    def set_valor(self, valor):
        """
        Establece los datos almacenados en el nodo.

        Args:
            value (Any): datos a almacenar en el nodo.
        """
        self.valor = valor
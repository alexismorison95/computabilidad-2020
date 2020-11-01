import pprint


class Graph:

    def __init__(self, edges_list: list):

        self.__graph = dict()
        self.edges_to_graph(edges_list)
    


    def edges_to_graph(self, edges: list):
        """Convierte una lista de de conexiones en un grafo.

        Parameters
        ----------
        edges : List
            Lista que contiene las conexiones entre nodos [(0, 1), (1, 2)]
        """

        for node1, node2 in edges:

            self.add_conection(node1, node2)
        
        self.remove_duplicates()
    


    def add_conection(self, node1: int, node2: int):
        """Permite agregar una conexion entre dos nodos de un grafo.

        Parameters
        ----------
        node1 : Int
            Nodo de salida

        node1 : Int
            Nodo de llegada
        """
        if node2:
            self.__graph.setdefault(node1, []).append(node2)
            self.__graph.setdefault(node2, []).append(node1)
        else:
            self.__graph.setdefault(node1, [])
    


    def remove_duplicates(self):
        """Remueve las conexiones duplicadas del grafo, hay que optimizar add_conection().
        """

        for node, conections in self.__graph.items():

            self.__graph[node] = list(set(conections))
    


    def remove_neighbours(self, node: int):
        """Permite remover todos los nodos vecinos de un grafo.

        Parameters
        ----------
        node : Int
            Nodo que se quiere eliminar junto con sus vecinos
        """

        conections = self.__graph[node]

        for node1 in conections:

            self.__graph.pop(node1, None)
        
        self.__graph.pop(node)



    def is_empty(self):
        """Permite saber si el grafo esta vacio, osea no hay ningun nodo.

        Returns
        ----------
        Boolean
            Valor booleano que indica si el grafo esta vacio (True),
            o no (False)
        """

        return True if len(self.__graph) == 0 else False



    def show_graph(self):
        """Permite representar el grafo para verlo por consola.
        """

        pretty_print = pprint.PrettyPrinter()

        pretty_print.pprint(self.__graph)

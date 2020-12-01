import pprint


class Graph:

    def __init__(self, edges_list: list):
        """Clase que permite generar grafos. Mas las funciones necesarias para trabajar con los mismos.

        Parameters
        ----------
        edges_list : List
            Lista de conexiones
        
        Returns
        ----------
        Graph Object
        """
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


    
    def is_not_empty(self):
        """Verifica si el grafo esta vacio.

        Returns
        ----------
        is_empty : Bool
            True si el grafo esta vacio, False de lo contrario
        """

        return bool(self.__graph)
    


    def minimum_degree(self):
        """Genera una lista de los nodos del grafo ordenados por grado, osea menor cantidad de aristas.

        Returns
        ----------
        degrees : List
            Lista de nodos ordenados por grado. [(nodo, grado)]
        """

        degrees = []

        for node, conections in self.__graph.items():
            degrees.append((node, len(conections)))
        
        degrees.sort(key=lambda x: x[1])

        return degrees




    def show_graph(self):
        """Permite representar el grafo para verlo por consola.
        """

        pretty_print = pprint.PrettyPrinter()
        pretty_print.pprint(self.__graph)

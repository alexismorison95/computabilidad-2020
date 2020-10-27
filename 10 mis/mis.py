import networkx as nx
from networkx.algorithms.approximation import independent_set
import numpy as np
import matplotlib.pyplot as plt
from graph import Graph
import copy
import time


class Mis:

    def __init__(self):

        self.__nodes = 0
        self.__matrix = None
        self.__edge_list = []
        self.graph = None
        self.mis_list = set()

    def random_incidence_matrix(self, nodes_count: int):
        """Permite generar una matriz de incidencia aleatoria, para poder generar
        un grafo.

        Parameters
        ----------
        nodes_count : Int
            Cantidad de nodos del grafo
        
        Returns
        ----------
        Numpy Array
            Matriz de incidencia en formato Numpy
        """

        self.__nodes = nodes_count

        self.__matrix = np.random.randint(0, 2, (self.__nodes, self.__nodes))

        self.generate_graph()

        return self.__matrix
    
    def set_incidence_matrix(self, matrix: np.ndarray):
        """Permite generar un grafo a partir de una matriz de incidencia.

        Parameters
        ----------
        matrix : Numpy Array
            Matriz de incidencia
        """

        self.__matrix = matrix
        
        x, _ = matrix.shape

        self.__nodes = x

        self.generate_graph()
    
    def set_edge_list(self, edge_list):
        """Permite generar un grafo a partir de una lista de conexiones.

        Parameters
        ----------
        edge_list : List
            Lista de caminos en forma de tuplas [(0, 1), (1, 2)]
        """

        self.__edge_list = edge_list

        nodes_list_aux = []
        self.__nodes = 0

        for node1, _ in edge_list:

            if node1 not in nodes_list_aux:
                nodes_list_aux.append(node1)
                self.__nodes += 1
        
        self.graph = Graph(self.__edge_list)
    
    def matrix_to_edges(self):
        """Permite convertir una matriz de incidencia en una lista de caminos.
        """

        self.__edge_list.clear()
        
        for i in range(self.__nodes):
            pos = -1

            for j in self.__matrix[i]:
                pos += 1

                if j == 1 and pos != i:
                    self.__edge_list.append((i, pos))

        return self.__edge_list
    
    def generate_graph(self):
        """Genera la lista de caminos y el grafo a partir de este.
        """

        self.matrix_to_edges()
        self.graph = Graph(self.__edge_list)
    
    def plot_graph(self, whit_mis=False):
        """Permite graficar el grafo.

        Parameters
        ----------
        whit_mis : Boolean
            Por defecto en False, solo grafica el grafo. Si es True, calcula
            el conjunto independiente maximo y grafica el grafo con este
        """

        temp_graph = nx.Graph()
        temp_graph.add_edges_from(self.__edge_list)

        if whit_mis:

            if len(self.mis_list) > 0:

                mis_nodes = []

                for node in self.mis_list:
                    mis_nodes.append(node)
                
                map_nodes = []

                for node in temp_graph:
                    if node in mis_nodes:
                        map_nodes.append('dodgerblue')
                    else:
                        map_nodes.append('lightskyblue')

                nx.draw_networkx(temp_graph, node_color=map_nodes)
            else:
                raise KeyError("Primero debe calcular el conjunto independiente maximo")
        
        else:
            nx.draw_networkx(temp_graph, node_color="dodgerblue")

        plt.axis("off")
        plt.show()
    
    def maximum_independent_set(self, verbose: bool):
        """Algoritmo que calcula el conjunto independiente maximo.

        Parameters
        ----------
        verbose : Boolean
            Si True, emprime un reporte de las operaciones
        """

        self.mis_list.clear()

        start_nodes = np.arange(self.__nodes)

        start = time.clock()

        for i in start_nodes:

            g = copy.deepcopy(self.graph)
            temp_mis = []
            node = i

            while not g.is_empty():
                
                if not node:
                    node = g.get_node()

                temp_mis.append(node)
                g.remove_neighbours(node)
                node = None

            if verbose:
                print('Evaluating = {}'.format(temp_mis))

            if len(temp_mis) > len(self.mis_list):
                self.mis_list = {node for node in temp_mis}

        end = time.clock() - start

        if verbose:
            print('\nExecution time {} seconds'.format(end))

        return self.mis_list

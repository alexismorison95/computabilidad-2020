import networkx as nx
from networkx.algorithms.approximation import independent_set
import numpy as np
import matplotlib.pyplot as plt
from graph import Graph
import copy
import time
import random


class Mis:

    def __init__(self):

        self.__nodes = 0
        self.__matrix = None
        self.__edge_list = []
        self.graph = None
        self.mis_list = set()
    


    def get_node_count(self):

        return self.__nodes


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
    


    def random_matrix_with_porc(self, nodes_count, prob):

        self.__nodes = nodes_count

        self.__matrix = np.zeros((self.__nodes, self.__nodes), dtype=np.int)

        for i in range(self.__nodes):
            for j in range(self.__nodes):
                
                if random.random() < prob:

                    self.__matrix[i][j] = 1
        
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
                raise ValueError("Primero debe calcular el conjunto independiente maximo")
        
        else:
            nx.draw_networkx(temp_graph, node_color="dodgerblue")

        plt.axis("off")
        plt.show()



    def inc_sub_conj(self, sub_conj):
        """Permite incrementar un vector de 0 y 1 como una suma binaria.

        Parameters
        ----------
        sub_conj : List
            Lista que representa a un subconjunto del grafo
        """

        size = self.__nodes

        carry = 0
        inc = '1'.zfill(size)

        size -= 1

        for node in range(self.__nodes):

            r = carry
            r += 1 if sub_conj[node] == 1 else 0
            r += 1 if inc[size] == '1' else 0

            sub_conj[node] = 1 if r % 2 == 1 else 0

            carry = 0 if r < 2 else 1

            size -= 1

        if carry != 0:
            return None

        return sub_conj



    def maximum_independent_set2(self, verbose: bool):
        """Algoritmo que calcula el conjunto independiente maximo.

        Parameters
        ----------
        verbose : Boolean
            Si True, imprime un reporte de las operaciones
        """

        sub_conj = [0]*self.__nodes

        self.mis_list.clear()

        start = time.clock()

        if not verbose:
                print('Evaluating subsets...')

        while sub_conj:

            g = copy.deepcopy(self.graph)
            temp_mis = []

            if verbose:
                print('Evaluating subset = {}'.format(sub_conj))
            
            for i in range(self.__nodes):
                if sub_conj[i] == 1:
                    
                    try:
                        g.remove_neighbours(i)
                        temp_mis.append(i)
                    except:
                        pass
            
            if len(temp_mis) > len(self.mis_list):
                self.mis_list = {node for node in temp_mis}

            # Genero otro subconjunto
            sub_conj = self.inc_sub_conj(sub_conj)
        
        end = time.clock() - start
        
        return self.mis_list, end

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import copy
import time
import random

from tools.graph import Graph



class Mis:

    def __init__(self):
        """Clase que permite obtener el Maximum Independet Set de un grafo.
        Tambien posee toda la funcionalidad necesaria para ejecutar los algoritmos.
        
        Returns
        ----------
        Mis Object
        """
        self.__nodes = 0
        self.__matrix = None
        self.__edge_list = []
        self.graph: Graph = None
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

        self.__generate_graph()

        return self.__matrix
    


    def random_matrix_with_porc(self, nodes_count: int, prob: float):
        """Permite generar una matriz de incidencia aleatoria con probabilidad de aristas, 
        para poder generar un grafo.

        Parameters
        ----------
        nodes_count : Int
            Cantidad de nodos del grafo
        
        prob : Float
            Probabilidad de generar aristas
        
        Returns
        ----------
        Numpy Array
            Matriz de incidencia en formato Numpy
        """

        self.__nodes = nodes_count

        self.__matrix = np.zeros((self.__nodes, self.__nodes), dtype=np.int)

        for i in range(self.__nodes):
            for j in range(self.__nodes):
                
                if random.random() < prob:
                    self.__matrix[i][j] = 1
        
        self.__generate_graph()

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

        self.__generate_graph()
    


    def set_edge_list(self, edge_list: list):
        """Permite generar un grafo a partir de una lista de conexiones.

        Parameters
        ----------
        edge_list : List
            Lista de caminos en forma de tuplas [(0, 1), (1, 2)]
        """

        self.__edge_list = edge_list
        nodes_list_aux = []

        for x, y in edge_list:
            nodes_list_aux.append(x)
            if y:
                nodes_list_aux.append(y)

        self.__nodes = len({node for node in nodes_list_aux})

        self.graph = Graph(self.__edge_list)



    def __matrix_to_edges(self):
        """Permite convertir una matriz de incidencia en una lista de caminos.
        """

        self.__edge_list.clear()
        
        for i in range(self.__nodes):
            pos = -1
            conexion = False

            for j in self.__matrix[i]:
                pos += 1

                if j == 1 and pos != i:
                    self.__edge_list.append((i, pos))
                    conexion = True
            
            if not conexion:
                self.__edge_list.append((i, None))

        return self.__edge_list
    


    def __generate_graph(self):
        """Genera la lista de caminos y el grafo a partir de este.
        """

        self.__matrix_to_edges()
        self.graph = Graph(self.__edge_list)
    


    def plot_graph(self, mis_result=None):
        """Permite graficar el grafo.

        Parameters
        ----------
        mis_result : List | Opcional
            resultado del algoritmo maximum independent set a graficar
        """

        temp_graph = nx.Graph()

        for x, y in self.__edge_list:
            if y:
                temp_graph.add_edge(x, y)
            else:
                temp_graph.add_node(x)

        if mis_result:

            mis_nodes = []

            for node in mis_result:
                mis_nodes.append(node)
            
            map_nodes = []

            for node in temp_graph:
                if node in mis_nodes:
                    map_nodes.append('dodgerblue')
                else:
                    map_nodes.append('lightskyblue')

            nx.draw_networkx(temp_graph, node_color=map_nodes)
        else:
            nx.draw_networkx(temp_graph, node_color="dodgerblue")

        plt.axis("off")
        plt.show()



    def is_overflow(self, sub_conj: list):
        """Permite verificar si se puede incrementar un subconjunto.

        Parameters
        ----------
        sub_conj : List
            Lista que representa a un subconjunto del grafo
        
        Returns
        ----------
        Boolean
            Si se puede incrementar o no
        """

        if sub_conj.count(1) == len(sub_conj):
            return True
        else:
            False



    def inc_sub_conj(self, sub_conj: list):
        """Permite incrementar un vector de 0 y 1 como una suma binaria.

        Parameters
        ----------
        sub_conj : List
            Lista que representa a un subconjunto del grafo
        
        Returns
        ----------
        List or None
            Subconjunto incrementado o None si no se puede incrementar
        """

        if self.is_overflow(sub_conj):
            return None
        else:
            j = len(sub_conj) - 1

            while sub_conj[j] == 1:
                sub_conj[j] = 0
                j -= 1
            
            sub_conj[j] = 1

            return sub_conj



    def maximum_independent_set_optimal(self, verbose: bool):
        """Algoritmo que calcula el conjunto independiente maximo. Complejidad = 2^n

        Parameters
        ----------
        verbose : Boolean
            Si True, imprime un reporte de las operaciones
        
        Returns
        ----------
        mis_list: Set
            Conjunto MIS

        end: Float
            Tiempo de ejecucion del algoritmo
        """

        sub_conj = [0]*self.__nodes
        self.mis_list.clear()

        start = time.clock()

        if not verbose:
                print('Evaluating all subset...')

        while sub_conj:

            g: Graph = copy.deepcopy(self.graph)
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
    


    def maximum_independent_set_heuristic(self, verbose: bool):
        """Algoritmo que calcula el conjunto independiente maximo heuristico, complejidad n

        Parameters
        ----------
        verbose : Boolean
            Si True, imprime un reporte de las operaciones
        
        Returns
        ----------
        mis: Set
            Conjunto MIS

        end: Float
            Tiempo de ejecucion del algoritmo
        """
        
        start = time.clock()

        if not verbose:
                print('Evaluating all subset...')
        
        g: Graph = copy.deepcopy(self.graph)
        mis_result = []
        cardinality = g.minimum_degree()

        while g.is_not_empty():

            node = cardinality.pop(0)

            if verbose:
                print('Evaluating node = {}, cardinality = {}'.format(node[0], node[1]))

            try:
                g.remove_neighbours(node[0])
                mis_result.append(node[0])
            except:
                pass
        
        end = time.clock() - start
        
        return {node for node in mis_result}, end


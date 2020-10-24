import networkx as nx
from networkx.algorithms.approximation import independent_set
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class Mis:

    def __init__(self):

        self.__nodes = None
        self.__matrix = None
        self.__edge_list = []
        self.temp_graph = None

    def random_incidence_matrix(self, nodes_count: int):

        self.__nodes = nodes_count

        self.__matrix = np.random.randint(0, 2, (self.__nodes, self.__nodes))

        return self.__matrix
    
    def set_incidence_matrix(self, matrix: np.ndarray):

        self.__matrix = matrix
        
        x, _ = matrix.shape

        self.__nodes = x
    
    def matrix_to_edges(self):

        self.__edge_list.clear()
        
        for i in range(self.__nodes):
            pos = -1

            for j in self.__matrix[i]:
                pos += 1

                if j == 1 and pos != i:
                    self.__edge_list.append((i, pos))
        
        return self.__edge_list
    
    def plot_graph(self):

        self.temp_graph = nx.Graph()
        self.matrix_to_edges()
        self.temp_graph.add_edges_from(self.__edge_list)

        nx.draw_networkx(self.temp_graph, node_color="dodgerblue")

        plt.axis("off")
        plt.show()
    
    def plot_graph_with_mis(self):

        self.temp_graph = nx.Graph()
        self.matrix_to_edges()
        self.temp_graph.add_edges_from(self.__edge_list)

        mis = self.maximum_independent_set()

        all_nodes = np.arange(self.__nodes)
        mis_nodes = []
        not_mis_nodes = []
        map_nodes = []

        for node in mis:
            mis_nodes.append(node)

        for node in all_nodes:
            if node not in mis_nodes:
                not_mis_nodes.append(node)

        for node in self.temp_graph:
            if node in mis_nodes:
                map_nodes.append('dodgerblue')
            else:
                map_nodes.append('skyblue')

        nx.draw_networkx(self.temp_graph, node_color=map_nodes) 

        plt.axis("off")
        plt.show()
    
    def maximum_independent_set(self):
        
        "TODO: Tengo que hacer mi algoritmo..."

        return independent_set.maximum_independent_set(self.temp_graph)

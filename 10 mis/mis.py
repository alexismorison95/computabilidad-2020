import networkx
from networkx.algorithms.approximation import independent_set
import numpy as np
import matplotlib.pyplot as plt


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

        self.temp_graph = networkx.Graph()

        self.matrix_to_edges()

        self.temp_graph.add_edges_from(self.__edge_list)

        labels = range(self.__nodes)

        networkx.draw_networkx(self.temp_graph, with_labels=labels)

        plt.axis("off")
        plt.show()
    
    def maximum_independent_set(self):

        return independent_set.maximum_independent_set(self.temp_graph)

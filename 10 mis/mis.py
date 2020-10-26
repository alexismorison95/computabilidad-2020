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
        self.mis_list = []

    def random_incidence_matrix(self, nodes_count: int):

        self.__nodes = nodes_count

        self.__matrix = np.random.randint(0, 2, (self.__nodes, self.__nodes))

        self.generate_graph()

        return self.__matrix
    
    def set_incidence_matrix(self, matrix: np.ndarray):

        self.__matrix = matrix
        
        x, _ = matrix.shape

        self.__nodes = x

        self.generate_graph()
    
    def set_edge_list(self, edge_list):

        self.__edge_list = edge_list

        nodes_list_aux = []
        self.__nodes = 0

        for node1, _ in edge_list:

            if node1 not in nodes_list_aux:
                nodes_list_aux.append(node1)
                self.__nodes += 1
        
        self.graph = Graph(self.__edge_list)
    
    def matrix_to_edges(self):

        self.__edge_list.clear()
        
        for i in range(self.__nodes):
            pos = -1

            for j in self.__matrix[i]:
                pos += 1

                if j == 1 and pos != i:
                    self.__edge_list.append((i, pos))

        return self.__edge_list
    
    def generate_graph(self):

        self.matrix_to_edges()
        self.graph = Graph(self.__edge_list)
    
    def plot_graph(self, whit_mis=False):

        temp_graph = nx.Graph()
        temp_graph.add_edges_from(self.__edge_list)

        if whit_mis:
            self.maximum_independent_set(verbose=True)

            print('\nMaximum independent set = {} \n'.format(self.mis_list))

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
            nx.draw_networkx(temp_graph, node_color="dodgerblue")

        plt.axis("off")
        plt.show()
    
    def maximum_independent_set(self, verbose: bool):

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
                self.mis_list = temp_mis

        end = time.clock() - start

        if verbose:
            print('\nExecution time {} seconds'.format(end))

        return self.mis_list

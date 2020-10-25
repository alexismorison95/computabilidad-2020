import pprint


class Graph:

    def __init__(self, edges_list):

        self.__graph = dict()
        self.edges_to_graph(edges_list)
    
    def edges_to_graph(self, edges):

        for node1, node2 in edges:

            self.add_conection(node1, node2)
        
        self.remove_duplicates()
    
    def add_conection(self, node1, node2):

        self.__graph.setdefault(node1, []).append(node2)
        self.__graph.setdefault(node2, []).append(node1)
    
    def remove_duplicates(self):

        for node, conections in self.__graph.items():

            self.__graph[node] = list(set(conections))
    
    def remove_neighbours(self, node):

        conections = self.__graph[node]

        for node1 in conections:

            self.__graph.pop(node1, None)
        
        self.__graph.pop(node)

    def is_empty(self):

        return True if len(self.__graph) == 0 else False
    
    def get_node(self, node=None):

        return list(self.__graph.keys())[0]
    
    def show_graph(self):

        pretty_print = pprint.PrettyPrinter()

        pretty_print.pprint(self.__graph)

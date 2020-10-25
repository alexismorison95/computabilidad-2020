from mis import Mis
import numpy as np

mis = Mis()

my_matrix = np.array(
    [[0, 1, 0, 1], 
    [1, 0, 1, 0],
    [0, 1, 0, 0], 
    [1, 0, 0, 0]]
)

#print(my_matrix)

mis.set_incidence_matrix(my_matrix)

#mis.random_incidence_matrix(4)

print('\nMaximum independent set = {} \n'.format(mis.maximum_independent_set()))

mis.plot_graph_with_mis()

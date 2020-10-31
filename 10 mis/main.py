from mis import Mis
import numpy as np

mis = Mis()

my_matrix = np.array(
    [[0, 1, 0, 1], 
    [1, 0, 1, 0],
    [0, 1, 0, 0], 
    [1, 0, 0, 0]]
)

mis.set_incidence_matrix(my_matrix)

mis_result = mis.maximum_independent_set2(True)

print('\nMaximum independent set = {}\n'.format(mis_result))

mis.plot_graph(whit_mis=True)

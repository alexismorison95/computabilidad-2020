import networkx
from networkx.algorithms.approximation import independent_set
import numpy as np
import matplotlib.pyplot as plt

nodes_count = 10

matrix = np.random.randint(0, 2, (nodes_count, nodes_count))

print(matrix)

lista = []

for i in range(nodes_count):

    pos = -1

    for j in matrix[i]:

        pos += 1

        if j == 1 and pos != i:
            lista.append((i, pos))


print(lista)


def graficar_matriz(lista, nodes_count):

    w = 4
    h = 3
    d = 70
    plt.figure(figsize=(w, h), dpi=d)

    g = networkx.Graph()

    g.add_edges_from(lista)

    labels = range(nodes_count)
    networkx.draw_networkx(g, with_labels=labels)
    plt.axis("off")
    plt.show()

    return g


graph = graficar_matriz(lista, nodes_count)

print(independent_set.maximum_independent_set(graph))

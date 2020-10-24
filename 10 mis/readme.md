# Algoritmo 10: maximum independent-set (Conjunto independiente maximo)

* Instancio la clase

    ```python
    mis = Mis()
    ```

* Opcion 1: Crear una matriz de incidencia aleatoria

    ```python
    cantidad_vertices = 4

    mis.random_incidence_matrix(cantidad_vertices)
    ```

* Opcion 2: Crear una matriz de incidencia propia y setearla

    ```python
    my_matrix = np.array(
    [[0, 1, 0, 1], 
    [1, 0, 1, 0],
    [0, 1, 1, 0], 
    [1, 1, 1, 0]]
    )

    mis.set_incidence_matrix(my_matrix)
    ```

* Graficar grafo y el grafo con mis

    ```python
    mis.plot_graph()

    mis.plot_graph_with_mis()
    ```

* Calcular el conjunto independiente maximo

    ## El algoritmo todavia no esta implementado, uso el de la biblioteca *networkx*

    ```python
    mis.maximum_independent_set())
    ```

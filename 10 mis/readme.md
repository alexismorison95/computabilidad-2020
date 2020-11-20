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

* Opcion 3: Crear una lista de conexiones y setearla

    ```python
    my_edge_list = [(0, 1), (1, 2), (1, 3), (2, 3), (4, 5), (5, 2)]

    mis.set_edge_list(my_edge_list)
    ```

* ### Opcion 4: Crear una matriz de incidencia aleatoria con un porcentaje de conexion entre nodos.
    > Opcion ideal para grafos con gran cantidad de nodos.

    ```python
    porcentaje = 0.2
    cant_vertices = 7

    matrix = mis.random_matrix_with_porc(cant_vertices, porcentaje)
    ```

* Mostrar grafo

    ```python
    mis.graph.show_graph()
    ```

* Calcular el conjunto independiente maximo

    ```python
    mis_result = mis.maximum_independent_set(verbose=True)
    ```

* Graficar grafo con mis

    ```python
    mis.plot_graph(mis_result)
    ```



# TP Final Teoria de la Computabilidad

## Algoritmo 02: SAT (Problema de satisfacibilidad booleana)

El problema SAT es el problema de saber si, dada una expresión booleana con variables y sin cuantificadores, hay alguna asignación de valores para sus variables que hace que la expresión sea verdadera. Por ejemplo, una instancia de SAT sería el saber si existen valores para 

    x1, x2, x3, x4 

tales que la expresión: 

    (x1 o x3) ^ (~x2 o x3 o ~x4)

 Sea verdadera.


### Orden computacional
    
    2^n

### Teorema de Cook

En teoría de la complejidad computacional, el Teorema de Cook establece lo siguiente: 

    El Problema de satisfacibilidad booleana (SAT) es NP-completo. (1971)


## Algoritmo 10: maximum independent-set (Conjunto independiente maximo)

![Conjunto independiente](https://upload.wikimedia.org/wikipedia/commons/e/ee/Mis_related_sets.png)

En teoría de grafos, un conjunto independiente o estable es un conjunto de vértices en un grafo tal que ninguno de sus vértices es adyacente a otro. Es decir, es un conjunto V de vértices tal que para ningún par de ellos existe alguna arista que los conecten.

### Orden computacional
    
    2^n
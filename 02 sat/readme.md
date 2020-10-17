# Algoritmo 02: SAT (Problema de satisfacibilidad booleana)

* Escribir una expresion booleana a evaluar

    ```python
    expression = '(a or b) and (not b or a)'
    ```

* Descomponer la cadena en tokens para obtener el nombre de las variables

    ```python
    tokenizer = Tokenizer(expression)
    var_names = tokenizer.tokenize()
    ```

* Instanciar la clase Sat y ejecutar el algoritmo

    ```python
    sat = Sat()
    sat.sat_algorithm(expression, var_names)
    ```



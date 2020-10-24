import time


class Sat:

    def __init__(self):

        self.__dictionary = dict()
        self.__var_list = []

    def list_to_dictionary(self, var_list: list):
        """Convierte una lista de variables a un diccionario o hash.

        Parameters
        ----------
        var_list : List
            Lista que contiene las variables en formato str
        """

        self.__var_list = var_list

        for var in self.__var_list:
            self.__dictionary[var] = 0

    def inc_dictionary(self):
        """Incrementa el diccionario para poder probar los distintos valores de
        las variables.

        Returns
        ----------
        Boolean
            Valor booleano que indica si se pudo incrementar el diccionario (True),
            o si hubo desbordamiento (False)
        """

        size = len(self.__var_list)

        carry = 0
        inc = '1'.zfill(size)

        size -= 1

        for var in self.__dictionary:

            r = carry
            r += 1 if self.__dictionary[var] == 1 else 0
            r += 1 if inc[size] == '1' else 0

            self.__dictionary[var] = 1 if r % 2 == 1 else 0

            carry = 0 if r < 2 else 1

            size -= 1

        if carry != 0:
            return False

        return True

    def sat_algorithm(self, expression: str, var_names: list, verbose: bool):
        """Implementacion de un algoritmo secuencial de orden computacional 2^n para el
        problema SAT (satisfacibilidad booleana), ya sea para expresiones en FNC, FND u otra forma.

        Parameters
        ----------
        expression : str
            Cadena de texto que representa la expresion a evaluar

        var_names : List
            Lista que contiene las variables en formato str

        verbose : bool
            Valor booleano que indica si se quiere hacer un reporte 
            de las operaciones del algoritmo
        
        Returns
        ----------
        Boolean
            Valor booleano que indica si se pudo satisfacer la expresion

        Dict | None
            Diccionario que muestra los valores de cada variable de la 
            expresion en caso de que la misma sea verdad, sino retorna None
        """

        start = time.clock()

        self.list_to_dictionary(var_names)

        loop_count = 0

        while True:

            loop_count += 1

            dictionary = self.__dictionary.copy()
            eval_expression = eval(expression, dictionary)

            if verbose:
                print('Evaluating = {}'.format(self.__dictionary))

            if eval_expression != 0:

                end = time.clock() - start

                if verbose:
                    print('\nExecution time {} seconds, in {} loops'.format(end, loop_count))

                return True, self.__dictionary

            if not self.inc_dictionary():

                end = time.clock() - start

                if verbose:
                    print('\nExecution time {} seconds, in {} loops'.format(end, loop_count))

                return False, None

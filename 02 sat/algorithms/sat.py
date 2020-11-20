import time


class Sat:

    def __init__(self):
        self.__dictionary = dict()
        self.__sub_conj = None
        self.__var_list = []
        self.__all_solutions = []



    def list_to_dictionary(self, var_list: list):
        """Convierte una lista de variables a un diccionario o hash.

        Parameters
        ----------
        var_list : List
            Lista que contiene las variables en formato str
        """

        self.__var_list = var_list
        self.__sub_conj = [0]*len(var_list)

        for var in self.__var_list:
            self.__dictionary[var] = 0



    def is_overflow(self):
        """Permite verificar si se puede incrementar un subconjunto.

        Returns
        ----------
        Boolean
            Si se puede incrementar o no
        """

        if self.__sub_conj.count(1) == len(self.__sub_conj):
            return True
        else:
            False



    def inc_sub_conj(self):
        """Permite incrementar un vector de 0 y 1 como una suma binaria.
        
        Returns
        ----------
        List or None
            Subconjunto incrementado o None si no se puede incrementar
        """

        if self.is_overflow():
            return None
        else:
            j = len(self.__sub_conj) - 1

            while self.__sub_conj[j] == 1:
                self.__sub_conj[j] = 0
                j -= 1
            
            self.__sub_conj[j] = 1

            return self.__sub_conj



    def inc_dictionary(self):
        """Incrementa el diccionario para poder probar los distintos valores de
        las variables.

        Returns
        ----------
        Boolean
            Valor booleano que indica si se pudo incrementar el diccionario (True),
            o si hubo desbordamiento (False)
        """

        if self.inc_sub_conj():
            for index, key in enumerate(list(self.__dictionary.keys())):
                self.__dictionary[key] = self.__sub_conj[index]
            
            return True
        else:
            return False



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

        while True:
            dictionary = self.__dictionary.copy()
            eval_expression = eval(expression, dictionary)

            if verbose:
                print('Evaluating = {}'.format(self.__dictionary))

            if eval_expression != 0:
                self.__all_solutions.append(self.__dictionary.copy())

            if not self.inc_dictionary():
                end = time.clock() - start

                return self.__all_solutions, end

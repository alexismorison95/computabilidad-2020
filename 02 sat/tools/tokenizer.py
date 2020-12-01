import re


class Tokenizer:

    def __init__(self, expression=''):
        self.__expression = expression
        self.__var_names = []
        self.var_ocurrencias = dict()
        self.__token_types = {
            'and': 0,
            'or': 0,
            'not': 0,
            '(': 0,
            ')': 0,
            'var': 0
        }



    def tokenize(self):
        """Permite Tokenizar una expresion.
        
        Returns
        ----------
        token_types : Dict
            Diccionario que cuenta los tipos de tokens en la expresion

        var_names : List
            Lista que contiene los nombres de las variables de la expresion
        """

        reg = re.compile(r'(\band\b|\bor\b|\bnot\b|\(|\))')

        tokens = reg.split(self.__expression)
        tokens = [t.strip() for t in tokens if t.strip() != '']

        for t in tokens:

            if t == 'and':
                self.__token_types['and'] += 1
            elif t == 'or':
                self.__token_types['or'] += 1
            elif t == 'not':
                self.__token_types['not'] += 1
            elif t == '(':
                self.__token_types['('] += 1
            elif t == ')':
                self.__token_types[')'] += 1
            else:
                if re.search('^[a-zA-Z0-9_]+$', t):

                    self.__token_types['var'] += 1

                    self.var_ocurrencias.setdefault(t, 0)
                    self.var_ocurrencias[t] += 1

                    if t not in self.__var_names:
                        self.__var_names.append(t)

        self.__var_names.sort()

        return self.__token_types, self.__var_names



    def tokenize_clause(self, clause: str):
        """Permite Tokenizar una clausula.

        Parameters
        ----------
        clause : str
            clausula de la cual se quiere obtener las variables
        
        Returns
        ----------

        var_list : List
            Lista que contiene los nombres de las variables de la clausula
        """

        var_list = []
        tokens = clause.split()

        for t in tokens:
            if t != 'or' and t != 'not':
                var_list.append(t)
        
        return var_list



    def get_clauses(self):
        """Permite obtener todas las clausulas de una expresion.
        
        Returns
        ----------

        clauses : List
            Lista que contiene las clausulas
        """

        reg = re.compile(r'\(|\)')

        tokens = reg.split(self.__expression)
        tokens = [t.strip() for t in tokens if t.strip() != '']

        clauses = []

        for t in tokens:
            if t != 'and':
                clauses.append(t)
        
        return clauses
import re


class Tokenizer:

    def __init__(self, expression):

        self.__expression = expression
        self.__var_names = []
        self.__token_types = {
            'and': 0,
            'or': 0,
            'not': 0,
            '(': 0,
            ')': 0,
            'var': 0
        }



    def tokenize(self):

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

                    if t not in self.__var_names:
                        self.__var_names.append(t)

        self.__var_names.sort()

        return self.__token_types, self.__var_names

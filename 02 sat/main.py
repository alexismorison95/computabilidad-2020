from tokenizer import Tokenizer
from sat import Sat


if __name__ == "__main__":

    expression = 'a and ((not a or (not c and d)) and (not e or (not e and not a)))'

    # Hago los tokens y obtengo los nombres de las variables
    tokenizer = Tokenizer(expression)

    tokens, var_names = tokenizer.tokenize()

    # Clase para implementar el algoritmo
    sat = Sat()

    print('\nExpression "' + expression + '" is', sat.sat_algorithm(expression, var_names))
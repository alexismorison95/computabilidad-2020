from tokenizer import Tokenizer
from sat import Sat

expression = 'a and (not a or (c and d)) and (e and (not e and not a))'

# Hago los tokens y obtengo los nombres de las variables
tokenizer = Tokenizer(expression)

tokens, var_names = tokenizer.tokenize()


# Clase para implementar el algoritmo
sat = Sat()


print('\nExpression "' + expression + '" is', sat.sat_algorithm(expression, var_names))

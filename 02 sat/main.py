from tokenizer import Tokenizer
from sat import Sat

if __name__ == "__main__":

    expression = '(a and b) and (c and  a)'

    tokenizer = Tokenizer(expression)
    tokens, var_names = tokenizer.tokenize()

    sat = Sat()

    result_sat = sat.sat_algorithm(expression, var_names, verbose=True)

    print('\nResult: Expression "{}" is {}'.format(expression, result_sat))

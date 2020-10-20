from tokenizer import Tokenizer
from sat import Sat
from generator import Generator

if __name__ == "__main__":

    expression = '(x6 or x2) and (x8 or x4) and (x1 or x5) and (x7 or x3)'

    gen = Generator(clause_count=4, literals_per_clause=2, variable_count=8, var_name='x')

    # expression = gen.generate()

    tokenizer = Tokenizer(expression)
    tokens, var_names = tokenizer.tokenize()

    sat = Sat()

    result_sat = sat.sat_algorithm(expression, var_names, verbose=True)

    print('\nResult: Expression "{}" is {}'.format(expression, result_sat))

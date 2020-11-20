from tokenizer import Tokenizer
from sat import Sat
from generator import Generator
#from tools.my_tools import save_result

if __name__ == "__main__":

    expression = '(a or b) and (c and not f and (a and not b))'

    gen = Generator(clause_count=4, literals_per_clause=2, variable_count=8, var_name='x')

    # expression = gen.generate()

    tokenizer = Tokenizer(expression)
    tokens, var_names = tokenizer.tokenize()

    sat = Sat()

    result_sat, time = sat.sat_algorithm(expression, var_names, verbose=False)

    print('\nExecution time {} seconds'.format(time))

    if len(result_sat) > 0:
        print('\nExpression "{}" is True'.format(expression))

        print('\nNumber of solutions is {}\n'.format(len(result_sat)))

        for result in result_sat:

            print(result)

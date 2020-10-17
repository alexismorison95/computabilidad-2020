from tokenizer import Tokenizer
from sat import Sat


if __name__ == "__main__":

    expression = '(a or b) and (not b or a)'

    tokenizer = Tokenizer(expression)
    tokens, var_names = tokenizer.tokenize()

    sat = Sat()

    print('\nExpression "' + expression + '" is', sat.sat_algorithm(expression, var_names))

import time


class Sat:

    def __init__(self):

        self.__dictionary = dict()
        self.__var_list = []
        self.__values = ''

    def list_to_dictionary(self, var_list: list):

        self.__var_list = var_list

        for var in self.__var_list:

            self.__dictionary[var] = 0
            self.__values += '0'

    def inc_dictionary(self):

        size = len(self.__var_list)

        # Normalize lengths
        x = self.__values.zfill(size)
        y = '1'.zfill(size)

        result = ''
        carry = 0

        self.__dictionary = dict()

        for i in range(size - 1, -1, -1):

            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0

            # r can be 0,1,2,3 (carry + x[i] + y[i])
            # and among these, for r==1 and r==3 you will have result bit = 1
            # for r==2 and r==3 you will have carry = 1

            self.__dictionary[self.__var_list[size - i - 1]] = int('1' if r % 2 == 1 else '0')

            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry != 0:
            return False

        self.__values = result.zfill(size)
        return True

    def sat_algorithm(self, expression: str, var_names: list, verbose: bool):

        start = time.clock()

        self.list_to_dictionary(var_names)

        loop_count = 0

        while True:

            loop_count += 1

            if verbose:
                print('Evaluating =', self.__dictionary)

            eval_expression = eval(expression, self.__dictionary)

            if eval_expression != 0:

                end = time.clock() - start

                if verbose:
                    print('\nExecution time {} seconds, in {} loops'.format(end, loop_count))

                return True

            if not self.inc_dictionary():

                end = time.clock() - start

                if verbose:
                    print('\nExecution time {} seconds'.format(end))

                return False

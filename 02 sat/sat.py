import time


class Sat:

    def __init__(self):

        self.__dictionary = {}
        self.__var_list = []
        self.__values = ''

    def list_to_dictionary(self, var_list):

        self.__var_list = var_list

        for var in self.__var_list:

            self.__dictionary[var] = 0
            self.__values += '0'

    def inc_values(self):

        size = len(self.__var_list)

        # Normalize lengths
        x = self.__values.zfill(size)
        y = '1'.zfill(size)

        result = ''
        carry = 0

        for i in range(size - 1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0

            # r can be 0,1,2,3 (carry + x[i] + y[i])
            # and among these, for r==1 and r==3 you will have result bit = 1
            # for r==2 and r==3 you will have carry = 1

            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry != 0:
            result = '1' + result

        self.__values = result.zfill(size)

        return len(self.__values)

    def inc_dictionary(self):

        self.__dictionary = {}

        for i in range(len(self.__values)):

            self.__dictionary[self.__var_list[i]] = int(self.__values[i])

    def sat_algorithm(self, expression, var_names):

        start = time.clock()

        self.list_to_dictionary(var_names)

        is_valid_expression = False

        while not is_valid_expression:

            print('Evaluating =', self.__dictionary)

            eval_expression = eval(expression, self.__dictionary)

            if eval_expression != 0:

                print('\nExecution time ' + str(time.clock() - start) + ' seconds')

                return True

            overflow = self.inc_values()

            if overflow > len(self.__var_list):

                print('\nExecution time ' + str(time.clock() - start) + ' seconds')

                return False

            self.inc_dictionary()

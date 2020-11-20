import random


class Generator:

    def __init__(self, clause_count: int, literals_per_clause: int, variable_count: int, var_name: str):
        self.clause_count = clause_count
        self.lit_clause = literals_per_clause
        self.var_count = variable_count
        self.var_name = var_name


    def generate(self):

        if self.var_count <= self.clause_count * self.lit_clause:

            sat = ''
            global_val = []
            is_valid_expression = False

            while not is_valid_expression:
                for i in range(self.clause_count):

                    sat += '('
                    var_list = []

                    for j in range(self.lit_clause):
                        var_to_add = self.generate_random_variable()

                        while var_to_add in var_list:
                            var_to_add = self.generate_random_variable()

                        var_list.append(var_to_add)

                        if var_to_add not in global_val:
                            global_val.append(var_to_add)

                        if random.randint(0, 1) == 0:
                            sat += 'not ' + var_to_add if j == self.lit_clause - 1 else 'not ' + var_to_add + ' or '
                        else:
                            sat += var_to_add if j == self.lit_clause - 1 else var_to_add + ' or '

                    sat += ')' if i == self.clause_count - 1 else ') and '

                if len(global_val) == self.var_count:
                    is_valid_expression = True
                else:
                    sat = ''
                    global_val = []

            return sat

        else:
            raise RuntimeError('literals_per_clause * clause_count must be >= variable_count')


    def generate_random_variable(self):

        return self.var_name + str(random.randint(1, self.var_count))

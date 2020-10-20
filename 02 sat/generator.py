import random


class Generator:

    def __init__(self, clause_count: int, literals_per_clause: int, variable_count: int, var_name: str):

        self.clause_count = clause_count
        self.lit_clause = literals_per_clause
        self.var_count = variable_count
        self.var_name = var_name

    def generate(self):

        sat = ''
        global_val = []

        while len(global_val) < self.var_count:

            global_val = []
            sat = ''

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

                        if j == self.lit_clause - 1:
                            sat += 'not ' + var_to_add
                        else:
                            sat += 'not ' + var_to_add + ' or '
                    else:
                        if j == self.lit_clause - 1:
                            sat += var_to_add
                        else:
                            sat += var_to_add + ' or '

                if i == self.clause_count - 1:
                    sat += ')'
                else:
                    sat += ') and '

        return sat

    def generate_random_variable(self):

        return self.var_name + str(random.randint(1, self.var_count))

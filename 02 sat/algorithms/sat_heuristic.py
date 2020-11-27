import time
import random
from tools.tokenizer import Tokenizer

class Sat:

    def __init__(self, var_list: list, clauses: list, individuals: int, mutation_p: float, crossover_p: float, generations: int):

        self.__var_list = var_list
        self.__clauses_list = clauses
        self.__solutions = []
        self.__individuals = individuals
        self.__mutation_p = mutation_p
        self.__crossover_p = crossover_p
        self.__generations = generations
        self.__tokenizer = Tokenizer()

    

    def list_to_dictionary(self, genome: list):
        """Convierte una lista de variables a un diccionario o hash.

        Parameters
        ----------
        var_list : List
            Lista que contiene las variables en formato str
        """

        dictionary = dict()

        for values in zip(self.__var_list, genome):
            dictionary[values[0]] = values[1]
        
        return dictionary



    def fitness(self, genome: list):

        clauses_sat = 0
        dictionary = self.list_to_dictionary(genome)

        for clause in self.__clauses_list:

            if eval(clause, dictionary.copy()) != 0:
                clauses_sat += 1
        
        return len(self.__clauses_list) - clauses_sat



    def crossover(self, mom: list, dad: list):

        child1, child2 = [], []

        for i in range(len(mom)):

            if random.sample([True, False], 1)[0]:
                child1.append(mom[i])
                child2.append(dad[i])
            else:
                child2.append(mom[i])
                child1.append(dad[i])
        
        return child1, child2



    def mutate(self, genome: list):

        m = random.random()

        if m < self.__mutation_p:
            pos = random.randint(0, len(genome)-1)

            if genome[pos] == 1:
                genome[pos] = 0
            else:
                genome[pos] = 1
        
        return genome



    def random_genome(self):

        genome = []

        for i in range(len(self.__var_list)):
            genome.append(random.randint(0, 1))
        
        return genome
    


    def create_population(self):

        population = []

        for _ in range(self.__individuals):
            population.append(self.random_genome())

        return population



    def get_fitness(self, individual):
        return individual[1]



    def selection(self, population: list):

        new_population = []

        for individual in population:
            new_population.append((individual, self.fitness(individual)))

        new_population.sort(key=self.get_fitness)
        new_population = new_population[:self.__individuals]

        population = []

        for individual in new_population:
            if individual[0] not in population:
                population.append(individual[0])

        return population
    


    def run_generations(self, population: list, start, verbose=True):

        for i in range(self.__generations):
            for _ in range(len(population)):

                is_crossover = random.random()
                if is_crossover < self.__crossover_p:

                    mom, dad = random.sample(population, 2)

                    c1, c2 = self.crossover(mom, dad)

                    c1 = self.mutate(c1)
                    c2 = self.mutate(c2)

                    population.append(c1)
                    population.append(c2)

            population = self.selection(population)
            
            if verbose:
                if i%1 == 0:
                    print(". Generation {}, Minimum Fitness = {}, time = {}".format(i, 
                    self.fitness(population[0]),
                    time.clock() - start))
            
            if self.fitness(population[0]) == 0:
                return population
        
        return population


    
    def sat_algorithm(self, verbose=True):

        population = self.create_population()

        start = time.clock()

        population = self.run_generations(population, start, verbose)
        
        population = self.selection(population)

        end = time.clock() - start

        results = []
        for individual in population:
            results.append(self.list_to_dictionary(individual))

        return results, end

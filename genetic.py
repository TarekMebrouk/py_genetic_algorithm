import random as rand
from .models import Solution

# constants
replacement_population = 42
replacement_probability = 0.3
incremental_population = 13
incremental_probability = 0.83
epochs = 100


class Genetic:

    # create new genetic meta-heuristic
    def __init__(self, algorithm_type):

        # initialize genetic algorithm type
        self.type = type
        if algorithm_type == "replacement":
            size = replacement_population
            self.probability = replacement_probability
        else:
            size = incremental_population
            self.probability = incremental_probability

        # generate random population to start
        self.population = []
        for i in range(size):
            solution = Solution()
            self.population.append(solution)

    # selection method
    def selection(self):
        # generate random number for choosing selection type
        selection_type = rand.randint(1, 4)

        # 1 : Selection by tournament
        if selection_type == 1:
            return self.tournament_selection()

        # 2 : Selection by roulette
        elif selection_type == 2:
            return self.roulette_selection()

        # 3 : Selection by row
        elif selection_type == 3:
            return self.row_selection()

        # 4 : Selection by elitism
        elif selection_type == 4:
            return self.elitism_selection()

    # Selection by tournament
    def tournament_selection(self):
        while True:
            index1 = rand.randint(0, len(self.population) - 1)
            index2 = rand.randint(0, len(self.population) - 1)
            if index1 != index2:
                selection = (self.population[index1], self.population[index2])
                return selection

    # Selection by roulette
    def roulette_selection(self):
        # sort population list
        sorted_population = sorted(self.population, key=lambda s: s.fitness, reverse=True)

        # calculate sum of population fitness
        fitness_sum = 0
        for solution in sorted_population:
            fitness_sum = fitness_sum + solution.fitness

        # generate two random
        selection = []
        for i in range(2):
            temp_sum = 0
            # generate random sum
            random_sum = rand.uniform(0, fitness_sum)
            index = 0
            while index < len(sorted_population) and temp_sum < random_sum:
                temp_sum = temp_sum + sorted_population[index].fitness
                index = index + 1
            selection.append(sorted_population[index - 1])

        return tuple(selection)

    # Selection by row
    def row_selection(self):
        # sort population list
        sorted_population = sorted(self.population, key=lambda s: s.fitness, reverse=True)

        # calculate sum of 1 .. size(Population)
        rows_sum = sum(range(1, len(sorted_population)))

        # generate two random
        selection = []
        for i in range(2):
            temp_sum = 0
            # generate random sum
            random_sum = rand.randint(1, rows_sum)
            index = 0
            while index < len(sorted_population) and temp_sum < random_sum:
                index = index + 1
                temp_sum = temp_sum + index
            selection.append(sorted_population[index - 1])

        return tuple(selection)

    # Selection by elitism
    def elitism_selection(self):
        # sort population list
        sorted_population = sorted(self.population, key=lambda s: s.fitness, reverse=True)

        # extract two max values
        selection = (sorted_population[0], sorted_population[1])
        return selection

    # crossing method
    def crossing(self, selection):
        # call crossing method by genetic algorithm type
        if self.type == "replacement":
            return self.replacement_crossing(selection)
        else:
            return self.incremental_crossing(selection)

    # replacement crossing
    def replacement_crossing(self, selection):
        x, y = selection

        # extract half of solution x
        x1 = []
        for i in range(len(x.array)//2):
            x1.append(x.array[i])

        x2 = []
        for i in range(len(x.array)//2, len(x.array)):
            x2.append(x.array[i])

        # extract half of solution y
        y1 = []
        for i in range(len(y.array)//2):
            y1.append(y.array[i])

        y2 = []
        for i in range(len(y.array)//2, len(y.array)):
            y2.append(y.array[i])

        # crossing solutions array
        x.array = x1 + y2
        y.array = y1 + x2

        crossing = (x, y)

        return crossing

    # incremental crossing
    def incremental_crossing(self, selection):
        x, y = selection

        # extract half of solution x
        x1 = []
        for i in range(len(x.array)//2):
            x1.append(x.array[i])

        # extract half of solution y
        y2 = []
        for i in range(len(y.array)//2, len(y.array)):
            y2.append(y.array[i])

        # crossing solutions array
        z = Solution()
        z.array = x1 + y2

        return z

    # incremental crossing
    def mutation(self, solution):
        if rand.random() < self.probability:
            index = rand.uniform(0, len(solution.array)-1)
            solution.array[index] = rand.randint(0, 100)
            return solution

    # incremental algorithm
    def incremental_algorithm(self):
        for i in range(epochs):
            # selection
            x, y = self.selection()

            # crossing
            x = self.crossing((x, y))

            # mutation
            random = rand.random()
            x = self.mutation(x)

            # evaluate new solution found
            x.evaluate()

            # replace the worst solution of previous iteration
            worst = min(self.population, key=lambda solution: solution.fitness)
            self.population.remove(worst)
            self.population.append(x)

    # replacement algorithm
    def replacement_algorithm(self):
        iteration = 0
        while iteration < epochs:
            # generate new population
            temporary_population = []
            while len(temporary_population) < len(self.population):
                # selection
                selection1, selection2 = self.selection()

                # crossing
                crossing1, crossing2 = self.crossing(selection=(selection1, selection2))

                # mutation
                mutation1 = crossing1
                mutation2 = crossing2
                random = rand.random()
                if random <= self.probability:
                    mutation1 = self.mutation(crossing1)

                random = rand.random()
                if random <= self.probability:
                    mutation2 = self.mutation(crossing2)

                # evaluate solutions found
                mutation1.evaluate()
                mutation2.evaluate()

                iteration = iteration + 2
                mutation1.view()
                mutation2.view()

                # append new solutions to temporary population
                temporary_population.append(mutation1)
                temporary_population.append(mutation2)

            # replace old population
            self.population = temporary_population

    # launch optimization algorithm
    def launch(self):
        # launch method by algorithm type
        if self.type == "replacement":
            self.replacement_algorithm()
        else:
            self.incremental_algorithm()

        # return best solution of population
        return max(self.population, key=lambda solution: solution.fitness)

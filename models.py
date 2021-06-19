import random as rand


class Solution:

    # create new solution
    def __init__(self):
        # array of solution
        self.array = []
        for i in range(50):
            self.array[i] = rand.randint(0, 100)

        # evaluate solution fitness
        self.fitness = 0
        self.evaluate()

    # evaluate auto-encoder solution
    def evaluate(self):
        self.fitness = rand.uniform(20, 30)

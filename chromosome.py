from random import randint, random, shuffle


class Chromosome:
    def __init__(self, problParam=None):
        self.problParam = problParam
        self.representation = list(range(problParam.dim))
        shuffle(self.representation)
        self.fitness = self.problParam.function(self.representation, self.problParam.network)

    def crossover(self, other_chromo, crossProbability):
        # if crossover fails, the offspring is identical to one of the parents
        if random() > crossProbability:
            offspring = Chromosome(self.problParam)
            offspring.representation = self.representation[:]
            return offspring

        newRepresentation = [-1] * len(self.representation)
        start = randint(0,len(self.representation)-2)
        end = randint(start+1, len(self.representation))
        slice = set(self.representation[start:end])
        newRepresIndex = end
        for index in range(start, end):
            newRepresentation[index] = self.representation[index]
        for index in range(end, len(self.representation)):
            if newRepresIndex < len(self.representation):
                if other_chromo.representation[index] not in slice:
                    newRepresentation[newRepresIndex] = other_chromo.representation[index]
                    newRepresIndex += 1
            else:
                newRepresIndex = 0
        for index in range(end):
            if newRepresIndex == len(self.representation):
                newRepresIndex = 0
            if other_chromo.representation[index] not in slice:
                newRepresentation[newRepresIndex] = other_chromo.representation[index]
                newRepresIndex += 1

        offspring = Chromosome(self.problParam)
        offspring.representation = newRepresentation
        return offspring


    def mutation(self, mutationProbability):
        first = randint(0,len(self.representation)-2)
        end = randint(first+1, len(self.representation)-1)
        end_element = self.representation[end]
        for i in reversed(range(first+1, end+1)):
            self.representation[i] = self.representation[i-1]
        self.representation[first+1] = end_element


    def __str__(self):
        return '\nChromo: ' + str(self.representation) + ' has fit: ' + str(self.fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.representation == c.representation and self.fitness == c.fitness

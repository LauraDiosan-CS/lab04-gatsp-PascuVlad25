from random import choices

from chromosome import Chromosome

class GA:
    def __init__(self, params=None, problParam=None):
        self.params = params
        self.problParams = problParam
        self.population = []

    def initialisation(self):
        for _ in range(self.params.populationSize):
            chromo = Chromosome(self.problParams)
            self.population.append(chromo)

    def evaluation(self):
        for chromo in self.population:
            chromo.fitness = self.problParams.function(chromo.representation, self.problParams.network)

    def bestChromosome(self):
        best = self.population[0]
        for chromo in self.population:
            if chromo.fitness < best.fitness:
                best = chromo
        return best

    def worstChromosome(self):
        worst = self.population[0]
        for chromo in self.population:
            if chromo.fitness > worst.fitness:
                worst = chromo
        return worst

    def selection(self):
        # Proportional, based on rank
        fit = []
        for i in range(len(self.population)):
            fit.append((i, self.population[i].fitness))
        fit = sorted(fit, key=lambda tup: tup[1], reverse=True)
        weight = [0] * len(self.population)
        n = len(fit)
        for i in range(n):
            weight[fit[i][0]] = i
        return choices([x for x in range(len(self.population))], weight)[0]

    def oneGenerationSteadyState(self):
        bestOff = Chromosome(self.problParams)
        for _ in range(self.params.populationSize):
            p1 = self.population[self.selection()]
            p2 = self.population[self.selection()]
            off = p1.crossover(p2, self.params.crossoverProb)
            off.mutation(self.params.mutationProb)
            off.fitness = self.problParams.function(off.representation, self.problParams.network)
            if off.fitness < bestOff.fitness:
                bestOff = off
        if bestOff.fitness < self.worstChromosome().fitness:
            self.population.remove(self.worstChromosome())
            self.population.append(bestOff)

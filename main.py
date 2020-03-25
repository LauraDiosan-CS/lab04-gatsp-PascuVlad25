from chromosome import Chromosome
from ga import GA
from in_out import *
from models.problemParams import ProblemParams
from models.gaParams import GAParams
from utilities import calculate_route_length

files = ['./input/easy_02_tsp.txt', './input/medium_02_tsp.txt', './input/hard_01_tsp.txt']
current_input_file_index = 2
input_file = files[current_input_file_index]
output_file = 'output.txt'


def main():
    graph = read_graph_from_file(input_file)

    gaParams = GAParams(populationSize=20, noOfGenerations=1000, crossoverProb=0.7, mutationProb=0.15)
    problemParams = ProblemParams(network=graph, dim=len(graph), function=calculate_route_length)

    ga = GA(gaParams, problemParams)
    ga.initialisation()
    ga.evaluation()

    allBestFitnesses = []
    generationsBest = []
    overallBest = Chromosome(problemParams)

    for generation in range(gaParams.noOfGenerations):
        ga.oneGenerationSteadyState()

        bestChromo = ga.bestChromosome()
        print('Best solution in generation ' + str(generation) + ' f(x) = ' + str(bestChromo.fitness))
        allBestFitnesses.append(bestChromo.fitness)
        generationsBest.append(bestChromo)
        if bestChromo.fitness < overallBest.fitness:
            overallBest = bestChromo

    print(overallBest.representation)
    print(calculate_route_length(overallBest.representation, problemParams.network))


main()
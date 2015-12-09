from __future__ import print_function, division

__author__ = 'amrit'

from EVM import EVM
from Errors import errors
import array
import random
from sk import rdivDemo
import json
import numpy
#from DE import DifferentialEvolution
from math import sqrt
from deap import algorithms
from deap import base
from deap import benchmarks
from deap.benchmarks.tools import diversity, convergence

#, hypervolume
from deap import creator
from deap import tools

def uniform(low, up, size=None):
    try:
        return [random.uniform(a, b) for a, b in zip(low, up)]
    except TypeError:
        return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]

def SPEA2(model=errors, NDIM=15, GEN=20,eta=0.5):
    MU = 100
    creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)
    toolbox = base.Toolbox()
    BOUND_LOW, BOUND_UP = 1.0, 20.0
    toolbox.register("attr_float", uniform, BOUND_LOW, BOUND_UP, NDIM)
    toolbox.register("r_list", tools.initIterate, creator.Individual, toolbox.attr_float)
    toolbox.register("population", tools.initRepeat, list, toolbox.r_list)
    toolbox.register("evaluate", model)
    toolbox.register("mate", tools.cxSimulatedBinaryBounded, eta=eta, low=BOUND_LOW, up=BOUND_UP)
    toolbox.register("mutate", tools.mutPolynomialBounded, eta=eta, low=BOUND_LOW, up=BOUND_UP, indpb=1/NDIM)
    toolbox.register("select", tools.selSPEA2)
    #binary tournament selection
    toolbox.register("selectTournament", tools.selTournament, tournsize=2)
    #binary tournament selection
    # Step 1 Initialization
    pop = toolbox.population(n=MU)
    archive = []
    curr_gen = 1
    min_val=[]


    while True:
        # Step 2 Fitness assignement
        for ind in pop:
            ind.fitness.values = toolbox.evaluate(ind)

        for ind in archive:
            ind.fitness.values = toolbox.evaluate(ind)

        # Step 3 Environmental selection
        archive  = toolbox.select(pop + archive, k=GEN)

        # Step 4 Termination
        if curr_gen >= GEN:
            final_set = archive
            break

        # Step 5 Mating Selection
        mating_pool = toolbox.selectTournament(archive, k=GEN)
        offspring_pool = map(toolbox.clone, mating_pool)

        # Step 6 Variation
        # crossover 100% and mutation 6%
        for child1, child2 in zip(offspring_pool[::2], offspring_pool[1::2]):
            toolbox.mate(child1, child2)

        for mutant in offspring_pool:
            if random.random() < 0.06:
                toolbox.mutate(mutant)

        pop = offspring_pool

        curr_gen += 1
    with open('./Pareto_Fronts/SPEA2-'+model.__name__+"-"+str(GEN)+"-"+str(eta)+'.txt', 'w') as f:
        for ind in final_set:
            f.write("%s %s\n" % (str(ind.fitness.values[0]), str(ind.fitness.values[1])))
            min_val.append(ind.fitness.values[0] + ind.fitness.values[1])
    return min_val
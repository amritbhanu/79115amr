from __future__ import print_function, division

__author__ = 'amrit'

from EVM import EVM
from Errors import errors
import array
import random
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

def NSGA2(model=errors, NDIM=15, GEN=20, eta=0.5):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)
    toolbox = base.Toolbox()
    BOUND_LOW, BOUND_UP = 1.0, 20.0
    toolbox.register("attr_float", uniform, BOUND_LOW, BOUND_UP, NDIM)
    toolbox.register("r_list", tools.initIterate, creator.Individual, toolbox.attr_float)
    toolbox.register("population", tools.initRepeat, list, toolbox.r_list)
    toolbox.register("evaluate", model)
    toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=BOUND_LOW, up=BOUND_UP, eta=eta)
    toolbox.register("mutate", tools.mutPolynomialBounded, low=BOUND_LOW, up=BOUND_UP, eta=eta, indpb=1.0/NDIM)
    toolbox.register("select", tools.selNSGA2)
    NGEN = GEN
    MU = 100
    CXPB = 0.9

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    logbook = tools.Logbook()
    logbook.header = "gen", "evals", "std", "min", "avg", "max"

    pop = toolbox.population(n=MU)

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # This is just to assign the crowding distance to the individuals
    # no actual selection is done
    pop = toolbox.select(pop, len(pop))
    min_val=[]
    record = stats.compile(pop)
    with open('./Pareto_Fronts/NSGA2-'+model.__name__+"-"+str(GEN)+"-"+str(eta)+'.txt', 'w') as f:
        f.write("%s %s\n" % (str(record.get('min')[0]), str(record.get('min')[1])))
        min_val.append(sum(record.get('min')))
        logbook.record(gen=0, evals=len(invalid_ind), **record)
        #print(logbook.stream)

        # Begin the generational process
        for gen in range(1, NGEN):
            # Vary the population
            offspring = tools.selTournamentDCD(pop, len(pop))
            offspring = [toolbox.clone(ind) for ind in offspring]

            for ind1, ind2 in zip(offspring[::2], offspring[1::2]):
                if random.random() <= CXPB:
                    toolbox.mate(ind1, ind2)

                toolbox.mutate(ind1)
                toolbox.mutate(ind2)
                del ind1.fitness.values, ind2.fitness.values

            # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
            fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit

            # Select the next generation population
            pop = toolbox.select(pop + offspring, MU)
            record = stats.compile(pop)
            min_val.append(sum(record.get('min')))
            f.write("%s %s\n" % (str(record.get('min')[0]), str(record.get('min')[1])))
            logbook.record(gen=gen, evals=len(invalid_ind), **record)
            #print(logbook.stream)

    return min_val

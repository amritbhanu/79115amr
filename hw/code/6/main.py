from __future__ import division, print_function
from random import seed
from time import time
from models import Schaffer, Osyczka2, Kursawe
from optimizers import simulatedAnnealing, maxWalkSat 

if __name__ == '__main__':
    t0=time()
    seed(t0)
    for model in [Schaffer, Osyczka2, Kursawe]:
 	for optimizer in [simulatedAnnealing, maxWalkSat]:
     	    print ("\n" * 3)
	    print ("Model", model.__name__)
     	    print ("Optimizer", optimizer.__name__)
     	    optimizer(model)
    print("\nRuntime: %s seconds" %str(time()-t0))

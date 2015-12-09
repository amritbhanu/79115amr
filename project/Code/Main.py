from __future__ import print_function, division

__author__ = 'amrit'

from EVM import EVM
from Errors import errors
from sk import rdivDemo
from NSGA2 import NSGA2
from SPEA2 import SPEA2
from hypervolume_runner import HyperVolume_wrapper

if __name__ == "__main__":

    optimizers = ["nsga2", "spea2"]
    models = [errors, EVM]
    mode_name = ["errors", "EVM"]
    NDIM = [14, 6]
    gen = [20, 40, 100]
    eta_n = [1, 10, 20]
    para = ["gen", "eta"]
    optimi = {}
    for x in optimizers:
        mode = {}
        for i in range(2):
            tune_dict = {}
            for j in para:
                if j == "gen":
                    waste = {}
                    for k in gen:
                        if x == "nsga2":
                            waste[k] = NSGA2(model=models[i], NDIM=NDIM[i], GEN=k, eta=0.5)
                        elif x == "spea2":
                            waste[k] = SPEA2(model=models[i], NDIM=NDIM[i], GEN=k, eta=0.5)
                    tune_dict[j] = waste
                elif j == "eta":
                    waste = {}
                    for k in eta_n:
                        if x == "nsga2":
                            waste[k] = NSGA2(model=models[i], NDIM=NDIM[i], GEN=50, eta=k)
                        elif x == "spea2":
                            waste[k] = SPEA2(model=models[i], NDIM=NDIM[i], GEN=50, eta=k)
                    tune_dict[j] = waste
            mode[mode_name[i]] = tune_dict
        optimi[x] = mode

    for y in mode_name:
        tmp_gen = []
        tmp_eta = []
        for x in optimizers:
            for k in gen:
                tmp_gen.append([y + "_" + x + "_" + "gen" + "_" + str(k)] + optimi[x][y]["gen"][k])
            for j in eta_n:
                tmp_eta.append([y + "_" + x + "_" + "eta" + "_" + str(j)] + optimi[x][y]["eta"][j])

        print(rdivDemo(tmp_gen))
        print(rdivDemo(tmp_eta))

    #This code has been referenced from https://github.com/ai-se/Spread-HyperVolume/tree/master/HyperVolume

    HyperVolume_wrapper()

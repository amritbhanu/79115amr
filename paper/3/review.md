a simple GA might be given by stating it will use binary representation, uniform crossover, bit-flip mutation, tournament selection, and generational replacement.
For a full specification, however, further details have to be given, for instance, the population size, the probability of mutation pm and crossover pc, and the tournament size. These data – called the algorithm parameters or strategy parameters.

we distinguish two major forms of setting parameter values: parameter tuning and parameter control. parameter tuning we mean the commonly practised approach that amounts to finding good values for the parameters before the run of the algorithm and then running the algorithm using these values, which remain fixed during the run. Parameter control forms an alternative, as it amounts to starting a run with initial parameter values that are changed during the run.

The technical drawbacks to parameter tuning based on experimentation can be summarised. (for a given type of EA, such as GAs).

single-point crossover

large mutation steps can be good in the early generations, helping the exploration of the search space, and small mutation steps might be needed in the late generations to help fine-tune the suboptimal chromosomes. use of static parameters itself can lead to inferior algorithm performance. A straightforward way to overcome the limitations of static parameters is by replacing a parameter p by a function p(t), where t is the generation counter. as indicated earlier,
the problem of finding optimal static parameters for a particular problem is already hard. Designing optimal dynamic parameters (that is, functions for p(t)) may be even more difficult.
HERE STATIC MEANS AT THE RUN TIME ITS FIXED AND NOT CHANGING DURING THE RUN.

parameter value p(t) changes are caused by a “blind” deterministic rule triggered by the progress of time t, without taking any notion of the actual progress in solving the problem, i.e., without taking into account the current state of the search. A well-known instance of this problem occurs in simulated annealing [49] where a so-called cooling schedule has to be set before the execution of the algorithm.

 use an EA for tuning an EA to a particular problem. This could be done using two EAs: one for problem solving and another one – the so-called metaEA – to tune the first one.  It could also be done by using only one EA that tunes itself to a given problem, while solving that problem. Selfadaptation

multivariate normal distribution
covariance matrix
successful mutations, where the offspring is better than the parent. corridor function (a bounded linear function)

non-isotropic functions, isotropic mutation.
In classifying parameter control techniques of an evolutionary algorithm, many aspects can be taken into account. For example:
1. What is changed? (e.g., representation, evaluation function, operators, selection process, mutation rate, population size, and so on)
2. How the change is made (i.e., deterministic heuristic, feedback-based heuristic, or self-adaptive)
3. The evidence upon which the change is carried out (e.g., monitoring performance of operators, diversity of the population, and so on)
4. The scope/level of change (e.g., population-level, individual-level, and so forth)



# Summary 
## (i) Paper : Arcuri, Andrea, and Gordon Fraser. "On parameter tuning in search based software engineering." In Search Based Software Engineering, pp. 33-47. Springer Berlin Heidelberg, 2011. [Paper](Read1.pdf)

## (ii) Keywords

  * (ii1)**Search Based Software Engineering** : SBSE converts a software engineering problem into a computational search problem that can be tackled with a metaheuristic. This involves defining a search space, or the set of possible solutions. This space is typically too large to be explored exhaustively, suggesting a metaheuristic approach. (wiki)
  * (ii2)**Parameter Tuning** : Parameter-tuning meant to optimize parameters of a classifier in order to maximize or minimize its objective; typically the maximization of efficiency or error minimization.
  * (ii3)**Crossover Rate** : Whenever two individuals are selected from the parent generation, this parameter specifies the probability with which they are crossed over. If they are not crossed over, then the parents are passed on to the next stage (mutation), else the offspring resulting from the crossover are used at the mutation stage.
  * (ii4)**Elitism Rate**  : Elitism describes the process that the best individuals of a population (its elite) automatically survive evolution.

## (iii) Brief Notes

  * (iii1) **Motivation** : Current researches don't talk about what population size to use for a genetic algorithm, which selection mechanism will be best? What other parameters to use to get the best result?
  * (iii2) **Related Work** :
   * **_Parameter Tuning and Control of ecolutionary algorithms_** : Eiben, A., Michalewicz, Z., Schoenauer, M., Smith, J.: Parameter control in evolutionary algorithms. Parameter Setting in Evolutionary Algorithms, 19–46 (2007).
   * **_Parameter Tuning on Common wisdom based settings_** : Smit, S., Eiben, A.: Parameter tuning of evolutionary algorithms: Generalist vs. specialist. Applications of Evolutionary Computation, 542–551 (2010).
   * **_Regression Tree based approach on Parameter Search Algorithm _** : Bartz-Beielstein, T., Markon, S.: Tuning search algorithms for real-world applications: A regression tree based approach. In: IEEE Congress on Evolutionary Computation (CEC), pp. 1111–1118 (2004).
   * **_GUIDE Tool for parameter tuning on search algorithm for industrial problem_** : Da Costa, L., Schoenauer, M.: Bringing evolutionary computation to industrial applications with GUIDE. In: Genetic and Evolutionary Computation Conference (GECCO), pp. 1467–1474 (2009).
  * (iii3) **Data** : They have generated the data using object-oriented software using EVOSUITE tool. This data consists of 20 software classes as case study. They considered this much to finsih the experiments in feasible time but still this led to more than one million experiments.
  * (iii4) **New Results** :
   * Different Parameter settings cause very large variance in the performance.
   * Default parameter settings perform relatively well, but are far from optimal on individual problem instances.
   * Tuning should be done on a very large sample of problem instances. Otherwise, the obtained parameter settings are likely to be worse than arbitrary default values.
   * Available search budget has strong impact on the parameter settings that should be used.

## (iv) Improvisations:
  * (iv1) A problem related to tuning is the search budget too. With a genetic algorithm population size will be more and this will take more computational time. Search budget work could have done separately to not conflict the results.
  * (iv2) Some problems cannont be deterministically found in reasonable time. This area could be a potential to work on.

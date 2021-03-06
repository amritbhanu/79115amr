# Summary 
## (i) Paper : Eiben, Agoston E., Zbigniew Michalewicz, Marc Schoenauer, and James E. Smith. "Parameter control in evolutionary algorithms." In Parameter setting in evolutionary algorithms, pp. 19-46. Springer Berlin Heidelberg, 2007. [Paper](Paper3.pdf)

## (ii) Keywords

  * (ii1) **Single-point crossover** : A single crossover point on both parents' organism strings is selected. All data beyond that point in either organism string is swapped between the two parent organisms. The resulting organisms are the children. (wiki)
  * (ii2) **Bit-flip mutation** : Bit-flip mutation is a common mutation operator for evolutionary algorithms applied to optimize functions over binary strings. Computing the probability distribution of fitness values of a binary string undergoing uniform bit-flip mutation. This probability distribution can be expressed as a polynomial in p, the probability of flipping each bit. (paper)
  * (ii3) **Multivariate normal distribution** : The multivariate normal distribution or multivariate Gaussian distribution, is a generalization of the one-dimensional (univariate) normal distribution to higher dimensions. One possible definition is that a random vector is said to be k-variate normally distributed if every linear combination of its k components has a univariate normal distribution. (wiki)
  * (ii4) **Covariance matrix**  : A covariance matrix (also known as dispersion matrix or variance–covariance matrix) is a matrix whose element in the i, j position is the covariance between the i-th and j-th elements of a random vector. Each element of the vector is a scalar random variable, either with a finite number of observed empirical values or with a finite or infinite number of potential values specified by a theoretical joint probability distribution of all the random variables. (wiki)

## (iii) Brief Notes

  * (iii1) **Motivation** : Setting the values of various parameters of an evolutionary algorithm is crucial for good performance. Special attention to setting parameters on-the-fly. This has the potential of adjusting the algorithm to the problem while solving the problem.
  * (iii2) **Hypotheses** : Parameters are not independent, but trying all different combinations systematically is practically impossible. The process of parameter tuning is time consuming, even if parameters are optimised one by one, regardless of their interactions. For a given problem the selected parameter values are not necessarily optimal, even if the effort made for setting them was significant.
  * (iii3) **Patterns** : Evolution strategies:
    * Gaussian Mutations: The main operator of ES is the Gaussian mutation, that adds centered normally distributed noise to the variables of the individuals. The most general Gaussian distribution is the multivariate normal distribution.
    * Adapting the Step-Size: The step-size of the Gaussian mutation gives the scale of the search.
    * Self-Adaptive ES: the parameters of the mutation (both the step-size and the covariance matrix) are attached to each individual, and are subject to mutation, too. Those personal mutation parameters range from a single step-size, leading to isotropic mutation, where all coordinates are mutated independently with the same variance, to the non-isotropic mutation
    * CMA-ES: a Clever Adaptation: The basic idea in CMA-ES is to use the path followed by the algorithm to deterministically update the different mutation parameters.
  * (iii4) **Sampling Procedures** :
	In classifying parameter control techniques of an evolutionary algorithm, many aspects can be taken into account. For example:
	1. What is changed? (e.g., representation, evaluation function, operators, selection process, mutation rate, population size, and so on)
	2. How the change is made (i.e., deterministic heuristic, feedback-based heuristic, or self-adaptive)
	3. The evidence upon which the change is carried out (e.g., monitoring performance of operators, diversity of the population, and so on)
	4. The scope/level of change (e.g., population-level, individual-level, and so forth)

## (iv) Improvisations:
  * (iv1) Varying Several Parameters Simultaneously.
  * (iv2) Population, Selection, Crossover, Mutation. These all operators need to be played with.
  * (iv3) Evaluation function needs to be verified with other functions too.

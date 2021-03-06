# Summary 
## (i) Paper : Fraser, Gordon, and Andrea Arcuri. "The seed is strong: Seeding strategies in search-based software testing." In Software Testing, Verification and Validation (ICST), 2012 IEEE Fifth International Conference on, pp. 121-130. IEEE, 2012. [Paper](Paper5.pdf)

## (ii) Keywords

  * (ii1) **Seeding** : Seeding is referred to any technique that exploits previous related knowledge to help solve the testing problem at hand. (paper)
  * (ii2) **Control dependence graph** : A control dependence graph is a representation, using graph notation, of all paths that might be traversed through a program during its execution. (wiki)
  * (ii3) **Tournament** : For each of the N positions it is needed to fill in the population, we generate 10 random test suites, and add only the one that has highest fitness. (Paper)
  * (ii4) **AllMethods**  : During the initialization, each time a new method call is inserted, it is not chosen randomly; instead, it is chosen based on a ring buffer of all methods. (paper)

## (iii) Brief Notes

  * (iii1) **Motivation** : The objective of such a search is to automatically generate test suites that maximize branch coverage. The problem should be solvable even without using previous knowledge.
  * (iii2) **Related Work** :
   * A seeding strategy is used in order to improve the ability of a classifier/regressor to generalize. W. B. Langdon and P. Nordin, “Seeding genetic programming populations,” in Proceedings of the European Conference on Genetic Programming (EuroGP), 2000, pp. 304–315
   * Seeding strategies is used to initialize a Genetic Programming population for optimizing execution time of a given input program. D. White, A. Arcuri, and J. Clark, “Evolutionary improvement of programs,” IEEE Transactions on Evolutionary Computation (TEC), vol. 15, no. 4, pp. 515–538, 2011.
   * Testing real-time systems to find worst case execution times. M. Tlili, S. Wappler, and H. Sthamer, “Improving evolutionary real-time testing,” in Genetic and Evolutionary Computation Conference (GECCO), 2006, pp. 1917–1924.
   * Seeding values taken from source code and documentation with the objective to reduce the human oracle costs. P. McMinn, M. Stevenson, and M. Harman, “Reducing
qualitative human oracle costs associated with automatically generated test data,” in Proceedings of the First International Workshop on Software Test Output Validation, ser. STOV ’10. New York, NY, USA: ACM, 2010, pp. 1–4.
  * (iii3) **Patterns** : SEEDING STRATEGIES FOR CLASS TESTING :
    * Evolutionary Testing of Classes
    * Seeding Constants
    * Optimizing the Initial Population
    * Incorporating Previous Solutions
  * (iii4) **Sampling Procedures** :
	- What is the impact of using constants from the bytecode for seeding?
	- Which are the best pre-processing techniques to seed an improved population before starting a SBST search?
	- Given a solution to improve from, which are the best seeding strategies to initialize a new population for SBST?

## (iv) Improvisations:
  * (iv1) Threats to construct validity are on how the performance of a testing technique is defined.
  * (iv2) Threats to internal validity might come from how the empirical study was carried out.
  * (iv3) Studying the interactions/relations of the different parameter configurations of EVOSUITE (e.g., population size and crossover probability) with the seeding strategies and the chosen search budget.

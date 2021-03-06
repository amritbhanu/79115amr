# Summary 
## (i) Paper : Poulding, Simon, John A. Clark, and Hélène Waeselynck. "A principled evaluation of the effect of directed mutation on search-based statistical testing." In Software Testing, Verification and Validation Workshops (ICSTW), 2011 IEEE Fourth International Conference on, pp. 184-193. IEEE, 2011. [Paper](Paper4.pdf)

## (ii) Keywords

  * (ii1) **Statistical testing** : Statistical testing generates test inputs by sampling from a probability distribution that is carefully chosen so that the inputs exercise all parts of the software being tested. (paper)
  * (ii2) **Directed mutation** : When evaluating potential solutions, feedback is normally returned to the search algorithm in the form a fitness metric, and this information is used to guide the algorithm’s selection operator. (paper)
  * (ii3) **Adaptive mutation** : The overall mutation rate is modified—over time, based on the recent changes in fitness, or by self-adaption as part of the representation—but the mutation operator itself is unchanged.. (wiki)
  * (ii4) **Response surface methodology** : RSM explores the relationships between several explanatory variables and one or more response variables. (wiki)

## (iii) Brief Notes

  * (iii1) **Motivation** : Sets of inputs are needed to detect more faults than test sets generated using traditional random and structural testing techniques. Significant improvement in algorithm performance, and so increases both the cost-effectiveness and scalability of search-based statistical testing.
  * (iii2) **Hypotheses** : The search algorithm proposed in this paper has the following key features :-
	a) Representation: They treated each argument independently since they will interact with each other in the code. Therefore a joint (multivariate) distribution is necessary, and a Bayesian network is used to represent such a distribution. A Bayesian network is a directed acyclic graph.
	b) Fitness metric - The fitness metric used here is an estimate of the probability lower bound achieved by the candidate probability distribution.
	c) Search Method: The search method used is stochastic hill climbing.
  * (iii3) **Patterns** : To implement directed mutation, they created three ‘mutation groups’ formed using the mutation operators:
    * 𝐺edge consists of the operators that modify edges in the Bayesian network: 𝑀add and 𝑀rem.
    * 𝐺bins consists of the remaining operators that modify bins directly: 𝑀len, 𝑀spl, 𝑀joi, and 𝑀prb, and applies to all bins.
    * 𝐺drct consists of the same bin-modifying operators as 𝐺bins, but applies them only to bins that contributed input vectors that executed the least-exercised structural element.
  * (iii4) **Sampling Procedures** :
	The choice of starting point, i.e., the initial algorithm parameter settings. This may have little effect if there is—as RSM assumes—a single optimum reachable by hill-climbing, but if there are multiple local optima, then the starting point may have a significant effect on the outcome. One possibility is to pick a random starting point and/or use a number of different starting points. The identification of the minimum along the path of steepest decision.

## (iv) Improvisations:
  * (iv1) There is a need to keep playing with the representation, fitness metric and search method itself— with the objective of further performance improvements.
  * (iv2) Search based statistical testing can be enhanced to generate test sequences, and to accommodate more complex test input data types.

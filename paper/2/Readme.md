# Summary 
## (i) Paper : Lamkanfi, Ahmed, Serge Demeyer, Quinten David Soetens, and Tim Verdonck. "Comparing mining algorithms for predicting the severity of a reported bug." In Software Maintenance and Reengineering (CSMR), 2011 15th European Conference on, pp. 249-258. IEEE, 2011. [Paper](Read2.pdf)

## (ii) Keywords

  * (ii1) **Naive Bayes Classifier** : Naive Bayes is a technique for constructing classifiers: models that assign class labels to problem instances, represented as vectors of feature values. It is a family of algorithms based on a common principle: all naive Bayes classifiers assume that the value of a particular feature is independent of the value of any other feature, given the class variable. Naive Bayes model works without accepting Bayesian probability or using any Bayesian methods. (wiki)
  * (ii2) **Severity** : The impact of a bug on the successful execution of the sorftware system. It is an absolute classification.
  * (ii3) **Stemming and stopwords** : Stemming is the process for reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form. Stop words are words which are filtered out before or after processing of natural language data. Though stop words usually refer to the most common words in a language. (wiki)
  * (ii4) **Tf-idf**  : Term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. The number of times a term occurs in a document is called its term frequency. An inverse document frequency factor is incorporated which diminishes the weight of terms that occur very frequently in the document set and increases the weight of terms that occur rarely. (wiki)

## (iii) Brief Notes

  * (iii1) **Motivation** : Current researches don't talk about what population size to use for a genetic algorithm, which selection mechanism will be best? What other parameters to use to get the best result?
  * (iii2) **Related Work** :
   * **_Parameter Tuning and Control of ecolutionary algorithms_** : Eiben, A., Michalewicz, Z., Schoenauer, M., Smith, J.: Parameter control in evolutionary algorithms. Parameter Setting in Evolutionary Algorithms, 19–46 (2007).
   * **_Parameter Tuning on Common wisdom based settings_** : Smit, S., Eiben, A.: Parameter tuning of evolutionary algorithms: Generalist vs. specialist. Applications of Evolutionary Computation, 542–551 (2010).
   * **_Regression Tree based approach on Parameter Search Algorithm_** : Bartz-Beielstein, T., Markon, S.: Tuning search algorithms for real-world applications: A regression tree based approach. In: IEEE Congress on Evolutionary Computation (CEC), pp. 1111–1118 (2004).
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

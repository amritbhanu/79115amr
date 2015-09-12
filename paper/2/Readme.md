# Summary 
## (i) Paper : Lamkanfi, Ahmed, Serge Demeyer, Quinten David Soetens, and Tim Verdonck. "Comparing mining algorithms for predicting the severity of a reported bug." In Software Maintenance and Reengineering (CSMR), 2011 15th European Conference on, pp. 249-258. IEEE, 2011. [Paper](Read2.pdf)

## (ii) Keywords

  * (ii1) **Naive Bayes Classifier** : Naive Bayes is a technique for constructing classifiers: models that assign class labels to problem instances, represented as vectors of feature values. It is a family of algorithms based on a common principle: all naive Bayes classifiers assume that the value of a particular feature is independent of the value of any other feature, given the class variable. Naive Bayes model works without accepting Bayesian probability or using any Bayesian methods. (wiki)
  * (ii2) **Severity** : The impact of a bug on the successful execution of the sorftware system. It is an absolute classification.
  * (ii3) **Stemming and stopwords** : Stemming is the process for reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form. Stop words are words which are filtered out before or after processing of natural language data. Though stop words usually refer to the most common words in a language. (wiki)
  * (ii4) **Tf-idf**  : Term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. The number of times a term occurs in a document is called its term frequency. An inverse document frequency factor is incorporated which diminishes the weight of terms that occur very frequently in the document set and increases the weight of terms that occur rarely. (wiki)

## (iii) Brief Notes

  * (iii1) **Motivation** : Severity of a bug is very important for a smooth working of a system. For predicting bug report severity, we should have a good classification algorithm. How much data/bug reports are necessary to train a data to get a reliable prediction? Are there couple of classifies which can predict severity very well?
  * (iii2) **Related Work** :
   * **_Predicting severity based on a rule learning technique_** : T. Menzies and A. Marcus, “Automated severity assessment of software defect reports,” in IEEE International Conference on Software Maintenance, 28 2008-Oct. 4 2008, pp. 346–355.
   * **_Classifying the reports as bugs or a feature request_** : G. Antoniol, K. Ayari, M. Di Penta, F. Khomh, and Y.-G. Gu´eh´eneuc, “Is it a bug or an enhancement?: a textbased approach to classify change requests,” in CASCON ’08: Proceedings of the conference of the center for advanced studies on collaborative research. ACM, 2008, pp. 304–318.
   * **_Categorization of bug reports on their descriptions_** : D. Cubranic and G. C. Murphy, “Automatic bug triage using text categorization,” in Proceedings of the Sixteenth International Conference on Software Engineering & Knowledge Engineering, June 2004, pp. 92–97.
   * **_Duplicate bug report detection_** : P. Runeson, M. Alexandersson, and O. Nyholm, “Detection of duplicate defect reports using natural language processing,” in Proceedings of the 29th international conference on Software Engineering, 2007.
  * (iii3) **Hypotheses** : 
    * Assumptions: Report contains summary of observed malfunction and a longer description. The reports are posted by users who have technical knowledge so they will write a detailed technical report.
    * Experiment: Extraction and organization of bug reports. Reports are prepocessed using the common steps of stopwords removal, stemming. Reports are categorized into svere and non-severe and classifier is trained. A number of classifiers are trained like Naive bayes, Naive Bayes Multinomial, 1-Nearest neighbor, SVM. For training the Tf-idf scores are maintained for feature extraction from data. They have used TPR (The rate of true positives) and FPR (the rate of false positives) for concluding the results.
  * (iii4) **New Results** :
   * The Naive Bayes Multinomial classifier has the best accuracy and is also the fastest when classifying the severity of reported bugs.
   * The Naive Bayes and Na¨ıve Bayes Multinomial classifiers are able to achieve stable accuracy the fastest. Also, we need about 250 bug reports of each severity when we train our classifier.
   * Each component tends to have its own particular way of describing severe and non-severe bugs. Thus, terms which are good indicators of the severity are usually component-specific.

## (iv) Improvisations:
  * (iv1) The classifier is trained on component basis, but a single report can belong to different components. Instead of single lables they should consider multi labels.
  * (iv2) They are dependent too much on the users giving detailed reports of bugs. There can be users who don't have that much technical knowledge.
  * (iv3) They have considered only 2 softwares bugs Eclipse and Genome. Validity needs to be checked on other softwares too.
  * (iv4) Reports aren't reliable as what they enter in description is according to their senses. But they might fall into different category.
  * (iv5) Duplicate bug reports will shift the training curve to fall each report into 1 category.

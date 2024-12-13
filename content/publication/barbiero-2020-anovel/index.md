---
title: A Novel Outlook on Feature Selection as a Multi-objective Problem
authors:
- Pietro Barbiero
- Evelyne Lutton
- Giovanni Squillero
- Alberto Tonda
date: '2020-01-01'
publishDate: '2024-12-13T08:56:18.631471Z'
publication_types:
- chapter
publication: '*Lecture Notes in Computer Science*'
doi: 10.1007/978-3-030-45715-0_6
abstract: Feature selection is the process of choosing, or removing, features to obtain
  the most informative feature subset of minimal size. Such subsets are used to improve
  performance of machine learning algorithms and enable human understanding of the
  results. Approaches to feature selection in literature exploit several optimization
  algorithms. Multi-objective methods also have been proposed, minimizing at the same
  time the number of features and the error. While most approaches assess error resorting
  to the average of a stochastic K-fold cross-validation, comparing averages might
  be misleading. In this paper, we show how feature subsets with different average
  error might in fact be non-separable when compared using a statistical test. Following
  this idea, clusters of non-separable optimal feature subsets are identified. The
  performance in feature selection can thus be evaluated by verifying how many of
  these optimal feature subsets an algorithm is able to identify. We thus propose
  a multi-objective optimization approach to feature selection, EvoFS, with the objectives
  to i. minimize feature subset size, ii. minimize test error on a 10-fold cross-validation
  using a specific classifier, iii. maximize the analysis of variance value of the
  lowest-performing feature in the set. Experiments on classification datasets whose
  feature subsets can be exhaustively evaluated show that our approach is able to
  always find the best feature subsets. Further experiments on a high-dimensional
  classification dataset, that cannot be exhaustively analyzed, show that our approach
  is able to find more optimal feature subsets than state-of-the-art feature selection
  algorithms.
links:
- name: URL
  url: https://doi.org/10.1007/978-3-030-45715-0_6
---

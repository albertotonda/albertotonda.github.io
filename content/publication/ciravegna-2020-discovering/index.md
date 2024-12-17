---
title: Discovering Hierarchical Neural Archetype Sets
date: '2020-07-01'
draft: true
publishDate: '2024-12-17T17:20:15.280732Z'
authors:
- Gabriele Ciravegna
- Pietro Barbiero
- Giansalvo Cirrincione
- Giovanni Squillero
- Alberto Tonda
publication_types:
- '6'
abstract: In the field of machine learning, coresets are defined as subsets of the
  training set that can be used to obtain a good approximation of the behavior that
  a given algorithm would have on the whole training set. Advantages of using coresets
  instead of the training set include improving training speed and allowing for a
  better human understanding of the dataset. Not surprisingly, coreset discovery is
  an active research line, with several notable contributions in literature. Nevertheless,
  restricting the search for representative samples to the available data points might
  impair the final result. In this work, neural networks are used to create sets of
  virtual data points, named archetypes, with the objective to represent the information
  contained in a training set, in the same way a coreset does. Starting from a given
  training set, a hierarchical clustering neural network is trained and the weight
  vectors of the leaves are used as archetypes on which the classifiers are trained.
  Experimental results on several benchmarks show that the proposed approach is competitive
  with traditional coreset discovery techniques, delivering results with higher accuracy,
  and showing a greater ability to generalize to unseen test data.
featured: false
publication: '*Progresses in Artificial Intelligence and Neural Systems*'
doi: 10.1007/978-981-15-5093-5_24
links:
- name: URL
  url: https://doi.org/10.1007/978-981-15-5093-5_24
---


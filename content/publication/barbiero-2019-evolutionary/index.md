---
title: Evolutionary discovery of coresets for classification
authors:
- Pietro Barbiero
- Giovanni Squillero
- Alberto Tonda
date: '2019-07-01'
publishDate: '2024-12-17T18:33:40.696779Z'
publication_types:
- paper-conference
publication: '*Proceedings of the Genetic and Evolutionary Computation Conference
  Companion*'
doi: 10.1145/3319619.3326846
abstract: When a machine learning algorithm is able to obtain the same performance
  given a complete training set, and a small subset of samples from the same training
  set, the subset is termed coreset. As using a coreset improves training speed and
  allows human experts to gain a better understanding of the data, by reducing the
  number of samples to be examined, coreset discovery is an active line of research.
  Often in literature the problem of coreset discovery is framed as i. single-objective,
  attempting to find the candidate coreset that best represents the training set,
  and ii. independent from the machine learning algorithm used. In this work, an approach
  to evolutionary coreset discovery is presented. Building on preliminary results,
  the proposed approach uses a multi-objective evolutionary algorithm to find compromises
  between two conflicting objectives, i. minimizing the number of samples in a candidate
  coreset, and ii. maximizing the accuracy of a target classifier, trained with the
  coreset, on the whole original training set. Experimental results on popular classification
  benchmarks show that the proposed approach is able to identify candidate coresets
  with better accuracy and generality than state-of-the-art coreset discovery algorithms
  found in literature.
links:
- name: URL
  url: https://doi.org/10.1145/3319619.3326846
---

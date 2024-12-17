---
title: Operator Selection using Improved Dynamic Multi-Armed Bandit
authors:
- Jany Belluz
- Marco Gaudesi
- Giovanni Squillero
- Alberto Tonda
date: '2015-01-01'
publishDate: '2024-12-17T18:33:40.512731Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2015 on Genetic and Evolutionary Computation Conference
  - GECCO ′15*'
doi: 10.1145/2739480.2754712
abstract: "Evolutionary algorithms greatly benefit from an optimal application of
  the different genetic operators during the optimization process: thus, it is not
  surprising that several research lines in literature deal with the self-adapting
  of activation probabilities for operators. The current state of the art revolves
  around the use of the Multi-Armed Bandit (MAB) and Dynamic Multi-Armed bandit (D-MAB)
  paradigms, that modify the selection mechanism based on the rewards of the different
  operators. Such methodologies, however, update the probabilities after each operator's
  application, creating possible issues with positive feedbacks and impairing parallel
  evaluations, one of the strongest advantages of evolutionary computation in an industrial
  perspective. Moreover, D-MAB techniques often rely upon measurements of population
  diversity, that might not be applicable to all real-world scenarios. In this paper,
  we propose a generalization of the D-MAB approach, paired with a simple mechanism
  for operator management, that aims at removing several limitations of other D-MAB
  strategies, allowing for parallel evaluations and self-adaptive parameter tuning.
  Experimental results show that the approach is particularly effective with frameworks
  containing many different operators, even when some of them are ill-suited for the
  problem at hand, or are sporadically failing, as it commonly happens in the real
  world."
links:
- name: URL
  url: https://doi.org/10.1145/2739480.2754712
---

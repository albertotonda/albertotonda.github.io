---
title: Bayesian Optimization for the Inverse Problem in Electrocardiography
authors:
- Alejandro Lopez-Rincon
- David Rojas-Velazquez
- Johan Garssen
- Sander W. van der Laan
- Daniel Oberski
- Alberto Tonda
date: '2023-12-01'
publishDate: '2024-12-13T18:55:57.960279Z'
publication_types:
- paper-conference
publication: '*2023 IEEE Symposium Series on Computational Intelligence (SSCI)*'
abstract: The inverse problem in electrocardiography is an illposed problem where
  the objective is to reconstruct the electrical activity of the epicardial surface
  of the heart, given the electrical activity on the thorax’ surface. In the forward
  problem, the electrical propagation from heart to thorax is modeled by the volume
  conductor equation with Dirichlet boundary conditions in the heart’s surface, and
  null flux coming from the thorax. The inverse problem, however, does not have a
  unique solution. In order to find solutions for the inverse problem, techniques
  such as Tikhonov regularization are classically used, but they often deliver unrealistic
  solutions. As an alternative, we propose a novel approach, where a fixed solution
  of the volume conductor model with a source in a forward scheme is used to solve
  the inverse problem. The unknown values for parameters of the fixed solution can
  be found using optimization techniques. Due to the characteristics of the problem,
  where each single evaluation of the cost function is expensive, we use a specialized
  CMA-ES-based Bayesian optimization technique, that can deliver good results even
  with a reduced number of function evaluations. Experiments show that the proposed
  approach can deliver improved results for in-silico simulations.
---

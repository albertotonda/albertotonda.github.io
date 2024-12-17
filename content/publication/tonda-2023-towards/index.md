---
title: Towards Evolutionary Control Laws for Viability Problems
date: '2023-01-01'
draft: true
publishDate: '2024-12-17T17:20:19.690880Z'
authors:
- Alberto Tonda
- Isabelle Alvarez
- Sophie Martin
- Giovanni Squillero
- Evelyne Lutton
publication_types:
- '1'
abstract: 'The mathematical theory of viability, developed to formalize problems related
  to natural and social phenomena, investigates the evolution of dynamical systems
  under constraints. A main objective of this theory is to design control laws to
  keep systems inside viable domains. Control laws are traditionally defined as rules,
  based on the current position in the state space with respect to the boundaries
  of the viability kernel. However, finding these boundaries is a computationally
  expensive procedure, feasible only for trivial systems. We propose an approach based
  on Genetic Programming (GP) to discover control laws for viability problems in analytic
  form. Such laws could keep a system viable without the need of computing its viability
  kernel, facilitate communication with stakeholders, and improve explainability.
  A candidate set of control rules is encoded as GP trees describing equations. Evaluation
  is noisy, due to stochastic sampling: initial conditions are randomly drawn from
  the state space of the problem, and for each, a system of differential equations
  describing the system is solved, creating a trajectory. Candidate control laws are
  rewarded for keeping viable as many trajectories as possible, for as long as possible.
  The proposed approach is evaluated on established benchmarks for viability and delivers
  promising results.'
featured: false
publication: '*Proceedings of the Genetic and Evolutionary Computation Conference*'
doi: 10.1145/3583131.3590415
links:
- name: URL
  url: https://doi.org/10.1145/3583131.3590415
---


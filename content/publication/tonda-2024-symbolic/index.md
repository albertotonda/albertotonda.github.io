---
title: Symbolic Regression of Confidence Intervals for Conformal Prediction
authors:
- Alberto Tonda
- Alejandro Lopez-Rincon
- David Rojas-Velazquez
- Evelyne Lutton
date: '2025-01-01'
publishDate: '2026-02-10T18:04:51.949355Z'
publication_types:
- paper-conference
publication: '*Artificial Evolution: 16th International Conference, Évolution Artificielle,
  EA 2024, Bordeaux, France, October 29–31, 2024, Revised Selected Papers*'
doi: 10.1007/978-3-032-07998-5_14
abstract: Conformal prediction is a class of algorithms designed to deliver confidence
  intervals around point predictions of models, with robust theoretical guarantees.
  Nevertheless, when dealing with regression problems, the original methodology always
  computes confidence intervals of the same size, independently of the magnitude of
  the predicted value y^, impairing the potential usefulness of the information. Several
  alternatives to properly scale the confidence intervals have been proposed in specialized
  literature, using assessments of the difficulty of predictions to produce wider
  intervals for more difficult points and tighter ones for easier predictions. However,
  each conformal prediction algorithm only exploits one specific type of information
  to evaluate the difficulty of a point prediction, such as Euclidean distance from
  points observed during training, or variance in the values of predictions for neighboring
  points. In this work, we introduce a novel symbolic regression approach to computation
  of confidence intervals. The algorithm can take into account all types of information
  considered by other conformal predictors at the same time, delivering human-interpretable
  equations that describe the amplitude of the intervals, tailored to the specific
  regression problem under evaluation. Experimental results show that the proposed
  approach outperforms other conformal predictors on an established benchmark suite
  of regression problems.
links:
- name: URL
  url: https://doi.org/10.1007/978-3-032-07998-5_14
---

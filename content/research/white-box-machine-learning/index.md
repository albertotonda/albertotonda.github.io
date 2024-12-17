---
title: Interpretable AI
summary: Obtaining human-readable, interpretable data-driven models
date: 2024-12-13
featured: true
tags:
  - Artificial intelligence
  - Research
  - Interpretability
---
Artificial Intelligence (AI) is a vast field with a considerable number of different approaches, ranging from symbolic AI to reinforcement learning. Most of the recent, impressive successes of AI are based on machine learning (ML), techniques able to learn predictive models for a given phenomenon directly from data.

While generally effective, models obtained through ML are often black boxes, as it is practically impossible for humans to infer their decision processes, due to their sheer complexity. For applications in fields like health and food science, black-box models are impractical, as for domain experts it is unaccaptable to just apply a solution without understanding it.

In my research, I tackled the question of obtaining human-readable data-driven models using different approaches.

<!-- ## White-box AI
Some of my early works dealt with creating white-box, human-readable ML models such as systems of Ordinary Differential Equations  [[gaucel2014learning]]({{< relref "/publication/gaucel-2014-learning/index.md" >}}), generation of computer code for a specific task using Genetic Programming~\cite{sanchez2011evolution}, or modeling the behavior of a player as a stochastic Finite State Machine.

## Integration of expert knowledge in AI

## Feature selection
Another way of making a ML model understandable is by reducing the number of features (variables) that it can use to take a decision; however, removing information might impair the performance of the algorithm. This is the principle behind _feature selection_, a subdomain of AI focused on finding the minimal amount of necessary information for the algorithm.

I developed novel techniques for unsupervised feature selection

## Old text below this point -->

Some of my early works dealt with [creating white-box, human-readable ML models such as systems of Ordinary Differential Equations (ODEs)]({{< relref "/publication/gaucel-2014-learning/index.md" >}}), and [integrating]({{< relref "/publication/tonda-2014-balancing/index.md" >}}) [expert knowledge]({{< relref "/publication/tonda-2013-amemetic/index.md" >}}) with [data-driven models]({{< relref "/publication/tonda-2012-bayesian/index.md" >}}). More recently I investigated the relationships between [datasets characteristics and generalization abilities of models]({{<relref "/publication/barbiero-2020-modeling/index.md">}}), and experimented with the translation of Explainable AI (XAI) techniques from the [field of image analysis to genomic data]({{<relref "/publication/lopezrincon-2021-classification/index.md">}}). Furthermore, I explored different approaches to feature and sample selection, the process of identifying the most compact sect of meaningful information to explain a ML algorithm decisions on a target problem, often employing Evolutionary Algorithms (EAs), see for example [Barbiero2020]({{<relref "/publication/barbiero-2020-generating/index.md">}}), [Ciravegna2020]({{<relref "/publication/ciravegna-2020-discovering/index.md">}}), [Barbiero2019]({{<relref "/publication/barbiero-2019-evolutionary/index.md">}}).

I am recognized as one of the experts of this niche combining EAs and ML, and as a consequence I co-organized tutorials on the subject in several specialized conferences (ACM GECCO, PPSN) plus an invited lecture in the summer school organized by [COST Action CA15140](https://imappnio.dcs.aber.ac.uk/) _Improving Applicability of Nature-Inspired Optimisation by Joining Theory and Practice_.
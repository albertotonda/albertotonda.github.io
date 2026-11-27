---
title: Deep learning in practice with pytorch
summary: Class on deep learning for Ph.D. students enrolled in Université Paris-Saclay, taught in English 
date: 2025-04-07
type: docs
math: false
tags:
  - deep learning
  - pytorch
  - teaching
image:
  image:
  caption: 'Embed rich media such as videos and LaTeX math'
---

The aim of this class is to provide students with a hands-on approach to deep learning, exploring functionalities of the pytorch library. Different applications of deep learning to relational data such as images and time sequences will presented, including the description of architectures like convolutional neural networks, recurrent neural networks, autoencoders, and transformers.

## Introduction to the class / Refresher on ML concepts
The first session is an introduction to the class and a (relatively quick) summary of basic machine learning concepts that will be extensively used in the following. 

[Slides - Introduction to the class, 2026](0-introduction.pdf)  
[Slides - Refresher on machine learning, 2026](0-machine-learning.pdf)  

[Colaboratory notebook with exercises on ML, 2026](https://colab.research.google.com/drive/1a5418oFw2pHwyALxXP1cqfAQfT76_8f5?usp=sharing)

## Basics of pytorch
Introduction to basic concepts of pytorch. Tensors, Modules, Optimizers, Loss functions.

[Slides - Refresher on neural networks and philosophy of pytorch, 2026](1-neural-networks-and-pytorch.pdf)  

[Colaboratory notebook with exercises on basic pytorch concepts, 2026](https://colab.research.google.com/drive/146pua5hpN8DcF958TaDqq3rO1tEgjX9h?usp=sharing)

## Intermediate pytorch concepts
Slightly more advanced pytorch concepts. Monitoring training performance, using Tensorboard, Stochastic gradient descent and derived techniques, Schedulers, Activation functions, Checkpointing.

[Slides - Intermediate pytorch concepts, 2026](1-intermediate-pytorch.pdf)  

[Colaboratory notebook with exercises on intermediate pytorch concepts, 2026](https://colab.research.google.com/drive/1RuT7FiEWVSgUF_aaSr8CIZCB6bEKV20R?usp=sharing)

## Convolutional neural networks
1. Basics of Convolutional Neural Networks (CNNs): convolution, pooling, architectures, applications.
2. An example applied to viral RNA/cDNA classification.

[Slides - Convolutional neural networks (CNNs), 2026](2-convolutional-neural-networks.pdf)  
[Slides - Case study: using CNNs for viral RNA classification, 2026](2-example-cnn-rna.pdf)  

[Colaboratory notebook with exercises on CNNs, 2026](https://colab.research.google.com/drive/1tSJZqGKw5EAuhUwG1ZTfB8ZeBa3VjqSi?usp=sharing)

## Remarks on deep learning
After having introduced the first modern neural network architectures, a few remarks on deep learning.
  
[Slides - General remarks on deep learning (i), 2026](1-remarks-on-neural-networks.pdf)

## Visualization techniques for CNNs
An overview of visualization techniques for CNNs.

[Slides - Visualization techniques for CNNs, 2026](2-cnn-visualization.pdf)  

[Colaboratory notebook with exercises on visualization techniques for CNNs, 2026](https://colab.research.google.com/drive/1k7hYg21Z6J8qh2f-jOmdWSljxXikTjW6?usp=sharing)

## Regularization
Quick excerpt on regularization techniques.

[Slides - Regularization, 2026](X-regularization.pdf)

## Embeddings
Basic notions of embeddings: what they are, and how to create them. Example of word embeddings with Word2Vec.

[Slides - Embeddings, 2026](4-embeddings.pdf)

[Colaboratory notebook with exercises on embeddings, 2026](https://colab.research.google.com/drive/1XNMAm2z8aQ07YZF0yn_r-MMJc3wQT3gi?usp=sharing)  
[Colaboratory notebook with a short example of a Variational Autoencoder, 2026](https://colab.research.google.com/drive/1fuX_Yyo9KSFsVn_3wPyvavXyd6NNwYdR?usp=sharing)

## Recurrent neural networks
Recurrent Neural Networks (RNNs) and more modern architectures, such as Long-Short-Term Memory Networks (LSTMs) and Gated Recurrent Units (GRUs).

[Slides - Recurrent neural networks, 2026](4-recurrent-neural-networks.pdf)

[Colaboratory notebook with exercises on RNNs, 2026](https://colab.research.google.com/drive/19RlceOejtIE_Ecn5kFPjEaXUrkdhO7YB?usp=sharing)

## Sequence to sequence
Introduction to the seq2seq architecture.

[Slides - Sequence to sequence, 2026](X-sequence-to-sequence.pdf)

[Colaboratory notebook with exercises on seq2seq, 2026](https://colab.research.google.com/drive/18ODB9ae2lkugSMUZw56KAlhBnlPVR7JX?usp=sharing)

## Terminology
Comments on common terminology found in neural network literature.

[Slides - Terminology, 2025](X-jargon.pdf)

## Attention and Transformers
Attention module and Transformer architectures.

[Slides - Attention, 2025](X-attention.pdf)

## Concept bottleneck models
Introduction to Concept Bottleneck Models and Concept Embedding Models.

[Slides - Concept bottlenecks, 2025](X-concept-bottlenecks.pdf)

## Current trends and future challenges

[Slides - Current trends and future challenges, 2025](X-remarks-ii-obstacles-and-perspectives-2025.pdf)

## Seminars

### The standard interpretable model (2026)
Advanced seminar on interpretable neural networks, given by [Dr. Pietro Barbiero](https://www.pietrobarbiero.eu/).

[Slides - The standard interpretable model, 2026 (white on black)](2026-11-SIM-INRAE.pdf)

[Slides - The standard interpretable model, 2026 (black on white, automatically generated by Claude Opus 5.5)](2026-11-SIM-INRAE-light.pdf)

### Graph neural networks (2025)
Advanced seminar on graph neural networks, given by [Dr. Gabriele Ciravegna](https://www.linkedin.com/in/gabriele-ciravegna-5a1130124).

[Slides - Graph neural networks (GNNs), 2025](seminar-ciravegna-graph-neural-networks.pdf)

[Colaboratory notebook with exercises on GNNs](https://colab.research.google.com/drive/1jX7uGTO4LIXoa-uIc44XzwqQW7DrSdOU?usp=sharing)

### Relational concept bottleneck models (2024)
Advanced seminar on relational concept bottleneck models, given by [Dr. Pietro Barbiero](https://www.pietrobarbiero.eu/).
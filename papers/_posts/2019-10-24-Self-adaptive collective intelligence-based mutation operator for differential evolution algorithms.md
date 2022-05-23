---
layout: paper
title: Self-adaptive collective intelligence-based mutation operator for differential evolution algorithms
image: "/lab_images/papers/Self-adaptive-collective.png"
authors: Jinhong Feng, Jundong Zhang, Chuan Wang & Minyi Xu 
year: 2020
ref: Jinhong Feng. et al. 2020. J Supercomput.
journal: "The Journal of Supercomputing volume 76, pages876–896"
pdf: "/pdfs/10.1007@s11227-019-03044-9.pdf"
doi: 10.1007/s11227-019-03044-9
type: journal
---

# Abstract

In conventional differential evolutionary (DE) algorithm, mutation operator has significant influence on generating new vectors by mixing existing target vectors randomly selected from the current population. Recently, many mutation operators, which usually employ the best individual or some high-quality individuals randomly chosen, have been proposed to improve searching capability. However, such designs may easily suffer from premature convergence trapped by local optima. To make a trade-off between exploration and exploitation capability, this paper proposes a novel collective intelligence (CI)-based mutation operator, which is named as “current-to-sa-ci-best.” In the presented mutation operator, the evolutionary information of m best target vectors is linearly combined to generate new mutant vectors. Besides, m is designed as an exponential-distributed random number which could be self-adapted based on successful records of m values alongside evolution. Moreover, this mutation operator could be applied to any DE algorithm without destroying existing search capability by adding a greedy selection operator. To verify its effectiveness, the proposed CI-based mutation strategy, which is named as SaCI, was embedded into some state-of-the-art DE variants on 28 CEC2013 benchmark functions. Numerical results have confirmed that the SaCI operator may be beneficial to DEs to some extent.


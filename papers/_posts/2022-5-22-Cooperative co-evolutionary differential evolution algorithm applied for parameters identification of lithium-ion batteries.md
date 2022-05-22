---
layout: paper
title: Cooperative co-evolutionary differential evolution algorithm applied for parameters identification of lithium-ion batteries
image: "https://cdn.jsdelivr.net/gh/MSPSLab/lab_images/papers/CCDE.png"
authors: Chuan Wang, Minyi Xu, Qinjin Zhang, Ruizheng Jiang, Jinhong Feng, Yi Wei, Yancheng Liu
year: 2022
ref: Chuan Wang. et al. 2022. Expert Systems with Applications
journal: "Expert Systems with Applications. 2022"
pdf: "/pdfs/CCDE.pdf"
doi: 10.1016/j.eswa.2022.117192
type: journal
---

# Abstract

Parameters identification of battery is a significant task for lithium-ion batteries. Some widely used techniques usually simplify the electrical circuit model (ECM) with non-linearity to a linear model or local linear model. However, by using such a methodology, the parameters in ECMs are not globally optimal, since the parameters may be not consistent at different linearized points. To address this issue, this paper proposed a cooperative co-evolution differential evolution (CCDE) algorithm to identify parameters of lithium-ion battery, without any linearization or pre-assumption. First, to describe the dynamic behaviors of battery, we presented a first-order RC equivalent circuit model ECM. Without making any approximation, improved Euler’s numerical method was utilized to solve the differential equations directly. Second, an optimizing objective function was built to minimize errors between the true and optimized terminal voltages. In that optimization model, parameters of battery (R0, RP and CP) and vOCV(t) at each sampling point were considered as variables to be optimized, resulting in a very high-dimension problem. Third, such an optimization problem was transformed into a large scale optimization problem (LSOP). Based on the character of parameters identification, we proposed a new m-decomposition method which is different from general grouping methods for benchmark functions and its corresponding differential evolution (DE) algorithm to solve this LSOP. Comprehensive experimental results demonstrated effectiveness of the proposed framework and methodology, compared with seven state-of-the-art cooperative co-evolution methods.
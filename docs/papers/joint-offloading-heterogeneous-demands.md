---
title: "Joint Task Offloading and Resource Allocation for LEO Satellite-Based Mobile Edge Computing Systems With Heterogeneous Task Demands"
authors: "Liang Zhong; Youyuan Li; Ming-Feng Ge; Mingjie Feng; Shiwen Mao"
year: "2025"
tags:
  - LEO
  - MEC
  - Offloading
  - Resource Allocation
  - DRL
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Joint Task Offloading and Resource Allocation for LEO Satellite-Based Mobile Edge Computing Systems With Heterogeneous Task Demands

**Authors:** Liang Zhong; Youyuan Li; Ming-Feng Ge; Mingjie Feng; Shiwen Mao  
**Year / version / venue:** IEEE Transactions on Vehicular Technology, 74(7), July 2025  
**Tags:** `LEO` `MEC` `Offloading` `Resource Allocation` `DRL`

## Original paper

[Open supplied PDF](../pdfs/joint-offloading-heterogeneous-demands.pdf){target="_blank" rel="noopener noreferrer"} · [DOI / preprint record](https://doi.org/10.1109/TVT.2025.3549119)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

This paper argues that a single shared utility function poorly represents heterogeneous IoT workloads. It builds task-specific utilities from a Gaussian mixture model (GMM), then jointly optimizes offloading, user association, transmit power, and computing resources. A layered iterative solver combines successive convex approximation with deep reinforcement learning. Both full and partial offloading are considered. [Abstract](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=1){target="_blank" rel="noopener noreferrer"}.

## Model and objective

Tasks can be processed using local, satellite-edge, and cloud resources. Their demands are represented through weighted resource/QoS dimensions; the worked example focuses on computing resources and delay. GMM soft clustering and expectation-maximization estimate preference weights. The optimization trades aggregate task utility against energy, subject to system feasibility constraints. [System model](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=3){target="_blank" rel="noopener noreferrer"}; [GMM utility formulation](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=6){target="_blank" rel="noopener noreferrer"}.

## Core approach

The original mixed-integer nonlinear problem is decomposed into continuous and discrete subproblems. Power and computing allocations are updated using convex optimization/SCA, while DQN-based decisions handle offloading and association. Partial offloading adds an update for the offloaded fraction. Algorithm 2 names the two schemes EDHTR and EDHPTR. [Sections IV-V](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=7){target="_blank" rel="noopener noreferrer"}; [Algorithms 1-2](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=11){target="_blank" rel="noopener noreferrer"}.

## Evaluation and key results

The simulated serving network contains **four LEO satellites at 500 km** and **40 mobile devices** in a 20 km by 20 km area. The underlying orbit configuration is Walker-based. The DQN has three hidden layers with 500, 250, and 120 neurons. [Section VI](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=11){target="_blank" rel="noopener noreferrer"}.

The abstract reports average user-utility improvements of **50% and 100%** over a single-metric and a typical classification-based utility model, respectively, and **30%-80%** gains over benchmark offloading/resource-allocation schemes. These refer to the paper's utility measurements, not equivalent percentage reductions in latency or energy. Training rewards stabilize after roughly 2,000 episodes in the reported runs. [Abstract](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=1){target="_blank" rel="noopener noreferrer"}; [Figures 5-7](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=12){target="_blank" rel="noopener noreferrer"}.

## Limitations

The experiments focus on two demand dimensions and a relatively small serving network. The paper states that analytical convergence verification of its DQN method is challenging; empirical convergence is not a global-optimality guarantee. Link-failure-induced task interruption and more varied network dynamics are identified as future work. [Complexity and convergence discussion](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=11){target="_blank" rel="noopener noreferrer"}; [conclusion](../pdfs/joint-offloading-heterogeneous-demands.pdf#page=15){target="_blank" rel="noopener noreferrer"}.

## Research connections and questions

*Follow-up interpretation:* the utility definition is as important as the optimizer. How sensitive are scheduling decisions to GMM fitting, utility scaling, and a mismatch between training tasks and future workloads? Compare utility gains alongside actual deadline misses and energy consumption.

## Related papers in this library

- [Dynamic Delay-Sensitive Observation-Data-Processing Task Offloading for Satellite Edge Computing: A Fully-Decentralized Approach](dynamic-delay-sensitive-offloading.md)
- [Satellite-MEC Integration for 6G Internet of Things: Minimal Structures, Advances, and Prospects](satellite-mec-integration.md)
- [Statistical Analysis for Energy-Efficient Satellite Edge Computing with Latency Guarantees](statistical-energy-latency-guarantees.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

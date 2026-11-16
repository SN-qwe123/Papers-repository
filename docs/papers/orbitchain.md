---
title: "OrbitChain: Orchestrating In-orbit Real-time Analytics of Earth Observation Data"
authors: "Zhouyu Li; Zhijin Yang; Huayue Gu; Xiaojian Wang; Yuchen Liu; Ruozhou Yu"
year: "2026"
tags:
  - LEO
  - Edge Computing
  - Real-Time
  - Scheduling
  - ML
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# OrbitChain: Orchestrating In-orbit Real-time Analytics of Earth Observation Data

**Authors:** Zhouyu Li; Zhijin Yang; Huayue Gu; Xiaojian Wang; Yuchen Liu; Ruozhou Yu  
**Year / version / venue:** arXiv:2508.13374v3, 10 February 2026. This copy contains placeholder conference/DOI fields; those fields are not treated as publication metadata.  
**Tags:** `LEO` `Edge Computing` `Real-Time` `Scheduling` `ML`

## Original paper

[Open supplied PDF](../pdfs/orbitchain.pdf){target="_blank" rel="noopener noreferrer"}

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Results have not been independently reproduced. Research questions are suggestions, not the authors' conclusions or JustinN's personal judgments. Source links use PDF viewer page numbers.

## Summary

OrbitChain distributes Earth-observation analytics across a leader–follower chain of satellites with overlapping ground coverage. A downstream satellite captures its own view of the target area and combines that local image with compact intermediate results from upstream satellites. This reduces the need to transfer large raw images between satellites. Offline profiling, joint function placement and resource allocation, and communication-aware pipeline routing support complex analytics workflows under limited compute, memory, and power budgets. [Source: abstract](../pdfs/orbitchain.pdf#page=1){target="_blank" rel="noopener noreferrer"}.

[arXiv version record](https://arxiv.org/abs/2508.13374v3)

## Research problem

Running an entire analytics workflow on every satellite can exceed memory or computing capacity. Splitting functions into a single compute pipeline can leave resources imbalanced. Sending raw imagery between satellites also imposes substantial communication costs. OrbitChain combines sensing and compute parallelism: different satellites contribute local observations and execute different portions of a workflow, while the planner balances processing capacity. [Source: design insights and overview](../pdfs/orbitchain.pdf#page=7){target="_blank" rel="noopener noreferrer"}.

## Core approach

- **Profile functions:** measure CPU/GPU processing speed, memory, power, and intermediate-data volume. The profiled intermediate outputs are five to six orders of magnitude smaller than raw sensing data in the studied functions.
- **Place and allocate:** a ground-side mixed-integer linear program determines function instances, CPU quotas, and GPU time slices under resource and power constraints. The implementation maximizes bottleneck capacity to provide headroom against fluctuations.
- **Route work:** construct pipelines through available function instances, favoring nearby satellites to reduce inter-satellite hops. Allocate tiles according to pipeline bottleneck capacity and update remaining capacity.
- **Orchestrate execution:** instantiate containerized functions, tag data by pipeline, match incoming intermediate results with local image tiles, and apply the planned GPU schedule.
- **Handle ground-track shifts:** restrict tiles to satellites that can actually observe them, assigning the more constrained coverage subsets first.

[Source: planner and runtime](../pdfs/orbitchain.pdf#page=7){target="_blank" rel="noopener noreferrer"}; [Source: resource allocation and routing](../pdfs/orbitchain.pdf#page=9){target="_blank" rel="noopener noreferrer"}; [Source: ground-track handling](../pdfs/orbitchain.pdf#page=10){target="_blank" rel="noopener noreferrer"}.

## Evaluation setup

The hardware-in-the-loop testbed uses **three NVIDIA Jetson Orin Nanos and four Raspberry Pi 4B devices**. Landsat 8 Cloud Cover images supply evaluation frames, divided into 640 × 640 tiles. Workflows combine cloud detection, land-use classification, crop monitoring, and water monitoring, with both chain-shaped and branching structures. Experiments use multiple frames; simulated channels reproduce constrained inter-satellite bandwidth. [Source: experimental setup](../pdfs/orbitchain.pdf#page=10){target="_blank" rel="noopener noreferrer"}.

Baselines are **data parallelism**, where each satellite hosts the whole workflow, and **compute parallelism**, which distributes one pipeline across satellites. A **load-spraying** variant isolates the impact of communication-aware routing. Metrics include completion ratio, inter-satellite traffic per frame, analyzable tile capacity, and end-to-end latency. [Source: baselines and metrics](../pdfs/orbitchain.pdf#page=11){target="_blank" rel="noopener noreferrer"}.

## Key results

| Finding | Experimental context |
| --- | --- |
| Nearly 100% completion on the evaluated Jetson workflows | Across the tested frame deadlines; baseline resource contention can cause queue buildup. |
| 60% higher completion ratio than compute parallelism | Raspberry Pi experiment at a 16-second frame deadline; not a universal speedup. |
| Up to 45% less inter-satellite traffic on Jetsons and 25% on Raspberry Pis | Compared with communication-agnostic load spraying. |
| 42% and 71% more analyzable tiles on average | Jetson and Raspberry Pi scaling studies, respectively, compared with compute parallelism; obtained through profile-based feasibility analysis rather than an enlarged physical testbed. |
| Under three minutes at 5 Kbps; under 30 seconds at 50 Kbps | A 100-tile frame in the three-satellite Jetson cloud–land-use–crop experiment. |

[Source: completion and traffic results](../pdfs/orbitchain.pdf#page=11){target="_blank" rel="noopener noreferrer"}; [Source: scaling and latency results](../pdfs/orbitchain.pdf#page=12){target="_blank" rel="noopener noreferrer"}.

## Limitations and reading cautions

A **frame deadline is a per-function throughput requirement** used to prevent queue buildup; it is not an end-to-end deadline for the whole workflow. End-to-end latency also includes processing, communication, and waiting for follower satellites to observe the target. Consequently, seconds-scale frame deadlines and minutes-scale end-to-end results are compatible in this model. [Source: latency discussion](../pdfs/orbitchain.pdf#page=12){target="_blank" rel="noopener noreferrer"}.

The approach depends on useful overlapping observations, predictable trajectories, and reliable profiling. A follower's later image is not necessarily identical to the leader's image, which matters for rapidly changing scenes. The reported experiments use terrestrial edge devices and emulated channels, not an operational orbital deployment. Larger-constellation capacity results rely on the optimization model and measured profiles.

## Research connections and questions

*Suggested follow-up:* quantify how scene changes between leader and follower observations affect accuracy. How should routing adapt to a satellite failure, stale profiles, or unexpected link degradation? Can model adaptation and pipeline placement be optimized together without destabilizing throughput?

## Related papers in this library

- [AdaOrb](adaorb.md): location-specific model adaptation complements OrbitChain's compute orchestration.
- [STAR-GS](star-gs.md): deadline-aware access to ground resources complements in-orbit processing.
- [Orbital Edge Computing: Nanosatellite Constellations as a New Class of Computer System](orbital-edge-computing-nanosatellites.md): an architectural predecessor discussed in OrbitChain.

## Personal notes

<!-- Add JustinN's own observations, annotations, and follow-up experiments here. -->

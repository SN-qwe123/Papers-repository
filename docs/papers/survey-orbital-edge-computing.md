---
title: "A comprehensive survey of orbital edge computing: Systems, applications, and algorithms"
authors: "Zengshan Yin; Changhao Wu; Chongbin Guo; Yuanchun Li; Mengwei Xu; Weiwei Gao; Chuanxiu Chi"
year: "2025"
tags:
  - LEO
  - Survey
  - Edge Computing
  - Scheduling
  - ML
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# A comprehensive survey of orbital edge computing: Systems, applications, and algorithms

**Authors:** Zengshan Yin; Changhao Wu; Chongbin Guo; Yuanchun Li; Mengwei Xu; Weiwei Gao; Chuanxiu Chi  
**Year / version / venue:** Chinese Journal of Aeronautics, 38(7), 103316. Available online November 2024.  
**Tags:** `LEO` `Survey` `Edge Computing` `Scheduling` `ML`

## Original paper

[Open supplied PDF](../pdfs/survey-orbital-edge-computing.pdf) · [DOI / preprint record](https://doi.org/10.1016/j.cja.2024.11.026)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

This survey maps orbital edge computing (OEC) across hardware, software, architectures, applications, optimization algorithms, and evaluation tools. Its central argument is that satellite mobility and tightly constrained energy, communication, storage, and compute resources make terrestrial edge-computing designs insufficient without adaptation. It connects systems research with task offloading, resource allocation, and satellite federated learning. Use it as a literature map and source of experimental design considerations, rather than as a new scheduling algorithm. [Source: abstract and introduction](../pdfs/survey-orbital-edge-computing.pdf#page=1).

## Research problem

How should researchers organize a field whose system architectures, objectives, and simulation assumptions vary substantially? The review distinguishes orbital computing from terrestrial MEC in architecture, computing, control, mobility, and applications. It covers both data produced on the ground and data produced in space. [Sections 2-4](../pdfs/survey-orbital-edge-computing.pdf#page=6).

## Main contributions and taxonomy

- **Systems:** satellite hardware and software, plus cloud/edge/end roles.
- **Applications:** Earth observation, scientific workloads, ground-origin services, and federated learning. FL is further organized around inter-satellite links and parameter-server placement.
- **Algorithms:** convex optimization, game theory, heuristics, and deep learning, including reinforcement learning.
- **Evaluation:** constellation configurations, performance metrics, network simulators, and testbeds. Examples discussed include STK, SNS3, Hypatia, SILLEO-SCNS, and StarPerf. These tools cover different parts of an OEC system; they are not interchangeable. [Sections 3-6](../pdfs/survey-orbital-edge-computing.pdf#page=9).

## Findings and research gaps

This is a review, so it has no single proposed algorithm with a controlled benchmark result. A useful methodological finding is that the same algorithm may behave very differently under different constellation configurations. The authors identify limited public telemetry and incomplete end-to-end OEC testbeds as barriers to credible evaluation. [Section 5](../pdfs/survey-orbital-edge-computing.pdf#page=16).

Open problems include mobility-aware resource optimization, resilient execution under failures, computing hardware design, caching, virtualization, containers and microservices, network slicing, and federated learning under varying data quality. [Section 7](../pdfs/survey-orbital-edge-computing.pdf#page=23).

## Limitations and reading cautions

The technology and deployment landscape reflects the review's publication period. Numerical improvements attributed to other works belong to those individual studies, not to a common benchmark run by this survey. Its observations about operational deployments should not be treated as current deployment statistics.

## Research connections and questions

*Interpretation for follow-up, not an additional claim of the paper:* before comparing schedulers, make a shared table of topology, visibility, workload, energy, and failure assumptions. A useful research question is how much a reported scheduling improvement survives when those assumptions are standardized.

## Related papers in this library

- [LEO Satellite Networking Relaunched: Survey and Current Research Challenges](leo-networking-relaunched.md)
- [Satellite-MEC Integration for 6G Internet of Things: Minimal Structures, Advances, and Prospects](satellite-mec-integration.md)
- [Orbital Edge Computing: Nanosatellite Constellations as a New Class of Computer System](orbital-edge-computing-nanosatellites.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

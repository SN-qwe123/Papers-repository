---
title: "Satellite-MEC Integration for 6G Internet of Things: Minimal Structures, Advances, and Prospects"
authors: "Yueshan Lin; Wei Feng; Yanmin Wang; Yunfei Chen; Yongxu Zhu; Ximu Zhang; Ning Ge"
year: "2023"
tags:
  - LEO
  - Survey
  - MEC
  - IoT
  - Architecture
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Satellite-MEC Integration for 6G Internet of Things: Minimal Structures, Advances, and Prospects

**Authors:** Yueshan Lin; Wei Feng; Yanmin Wang; Yunfei Chen; Yongxu Zhu; Ximu Zhang; Ning Ge  
**Year / version / venue:** Supplied arXiv preprint, arXiv:2308.14992v1, August 29, 2023  
**Tags:** `LEO` `Survey` `MEC` `IoT` `Architecture`

## Original paper

[Open supplied PDF](../pdfs/satellite-mec-integration.pdf){target="_blank" rel="noopener noreferrer"} · [DOI / preprint record](https://arxiv.org/abs/2308.14992)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

This survey describes satellite-MEC integration using three minimal structures, distinguished by where computation occurs relative to satellite links. It reviews each structure's offloading, placement, and resource-management problems, then discusses combinations. Its main contribution is an architectural vocabulary for comparing heterogeneous systems, rather than one universally optimal offloading policy. [Abstract](../pdfs/satellite-mec-integration.pdf#page=1){target="_blank" rel="noopener noreferrer"}.

## Architectural taxonomy

| Structure | Computing placement | Main implication |
| --- | --- | --- |
| Computing-in-Forward-link (CIF) | Nearby aerial or terrestrial edge resources on the user side | Low local latency, but limited platform resources and coverage |
| Computing-on-Orbit (COO) | MEC resources aboard satellites | Avoid some long paths to ground compute, at the cost of space hardware and mobility constraints |
| Computing-after-Feeder-link (CAF) | Gateway-side ground resources reached through satellite links | Access stronger ground compute, while retaining communication delay and feeder-link dependence |

The paper treats larger integrated networks as combinations of these structures, rather than assuming all satellite MEC means onboard processing. [Sections II-V](../pdfs/satellite-mec-integration.pdf#page=2){target="_blank" rel="noopener noreferrer"}.

## Main findings

Important decisions span server placement, service placement, task offloading, cooperative computing, communication resource allocation, and handoff. The right design depends on spatially heterogeneous demand and on the different capabilities of the participating platforms. Tables summarize prior studies instead of reporting a new common benchmark. [Sections III-VI](../pdfs/satellite-mec-integration.pdf#page=3){target="_blank" rel="noopener noreferrer"}.

A particularly useful research gap is **medium-timescale adjustment**: seconds-to-milliseconds resource decisions and months-to-years infrastructure planning do not fully cover changes in service geography and demand. The survey proposes hierarchical orchestration and a hierarchy of adjustment timescales. [Section VII and Figure 4](../pdfs/satellite-mec-integration.pdf#page=11){target="_blank" rel="noopener noreferrer"}.

## Open questions

The agenda includes AI-supported control, supporting AI workloads over the integrated network, security/resource tradeoffs, coordination with sensing and navigation, and energy efficiency. For example, security approaches that require extensive synchronization may conflict with constrained satellite connectivity. [Section VII](../pdfs/satellite-mec-integration.pdf#page=12){target="_blank" rel="noopener noreferrer"}.

## Limitations

This is a 2023 preprint version supplied by the user; later publication status is not inferred. The three-structure decomposition is a conceptual framework, not a tested guarantee that combinations can be optimized independently. Reviewed studies use different models and objectives, so their numerical results should not be ranked directly.

## Research connections and questions

*Follow-up interpretation:* first label every comparison algorithm by where its data originates and where its compute runs. This prevents unfair comparisons between ground-user offloading, onboard EO processing, and gateway-assisted computing. Consider joint service placement at a medium timescale and per-task scheduling at a faster timescale.

## Related papers in this library

- [A comprehensive survey of orbital edge computing: Systems, applications, and algorithms](survey-orbital-edge-computing.md)
- [Joint Task Offloading and Resource Allocation for LEO Satellite-Based Mobile Edge Computing Systems With Heterogeneous Task Demands](joint-offloading-heterogeneous-demands.md)
- [LEO Satellite Networking Relaunched: Survey and Current Research Challenges](leo-networking-relaunched.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

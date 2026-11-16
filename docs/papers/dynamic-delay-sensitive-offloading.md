---
title: "Dynamic Delay-Sensitive Observation-Data-Processing Task Offloading for Satellite Edge Computing: A Fully-Decentralized Approach"
authors: "Ruipeng Zhang; Yanxiang Feng; Yikang Yang; Xiaoling Li; Hengnian Li"
year: "2024"
tags:
  - LEO
  - Earth Observation
  - Offloading
  - Scheduling
  - Distributed Systems
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Dynamic Delay-Sensitive Observation-Data-Processing Task Offloading for Satellite Edge Computing: A Fully-Decentralized Approach

**Authors:** Ruipeng Zhang; Yanxiang Feng; Yikang Yang; Xiaoling Li; Hengnian Li  
**Year / version / venue:** Remote Sensing, 16(12), 2184  
**Tags:** `LEO` `Earth Observation` `Offloading` `Scheduling` `Distributed Systems`

## Original paper

[Open supplied PDF](../pdfs/dynamic-delay-sensitive-offloading.pdf){target="_blank" rel="noopener noreferrer"} · [DOI / preprint record](https://doi.org/10.3390/rs16122184)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

The paper studies where and in what order to execute delay-sensitive observation-processing tasks when satellites can exchange information only with neighboring satellites. It formulates an assignment-and-sequencing problem and proposes the Performance Impact-based Task Offloading algorithm, PITO. PITO combines local task insertion/removal with distributed consensus, avoiding a central offloading server. A second mechanism limits the amount of rescheduling needed when new tasks arrive. [Abstract](../pdfs/dynamic-delay-sensitive-offloading.pdf#page=1){target="_blank" rel="noopener noreferrer"}.

## Model and objective

The objective combines energy consumption with **deadline overrun magnitude**: the positive part of completion time minus deadline. It is therefore not simply a count of missed deadlines, nor a hard guarantee that every deadline is met. Constraints include one execution satellite per task, satellite memory and energy limits, and task ordering. [Equation 10 and constraints 11-18](../pdfs/dynamic-delay-sensitive-offloading.pdf#page=7){target="_blank" rel="noopener noreferrer"}.

## Core approach

1. Satellites maintain local task sequences and quantify the cost impact of inserting or removing a task.
2. Neighbor-to-neighbor exchanges and consensus resolve competing assignments.
3. Task removal adjusts local sequences after consensus.
4. For newly arriving tasks, a match-up re-offloading mechanism preserves parts of the existing schedule and prunes candidate insertion positions to reduce extra work and unnecessary data transfers. [Sections 4.1-4.5](../pdfs/dynamic-delay-sensitive-offloading.pdf#page=7){target="_blank" rel="noopener noreferrer"}.

## Evaluation and key results

The MATLAB evaluation uses STK-derived positions for six Walker Delta constellations, with 6-66 computing satellites and small, medium, and large task sets. It compares PITO with CNP, DETS, and ADMM using relative objective value, communication count, and running time. Each configuration includes repeated randomized instances and runs. [Tables 3-5](../pdfs/dynamic-delay-sensitive-offloading.pdf#page=15){target="_blank" rel="noopener noreferrer"}.

PITO obtains the best relative objective and communication-count results in almost all tested combinations; the authors note exceptions where DETS performs best. For the reported case with 80 observation satellites, PITO uses **80.35% fewer communication exchanges than ADMM** and **74.29% fewer than DETS**. These percentages refer to that experiment, not every topology. [Section 5.2](../pdfs/dynamic-delay-sensitive-offloading.pdf#page=16){target="_blank" rel="noopener noreferrer"}; [Figure 9 discussion](../pdfs/dynamic-delay-sensitive-offloading.pdf#page=21){target="_blank" rel="noopener noreferrer"}.

## Limitations

The evidence is simulation-based. The constellation set includes computing satellites at 3,000 and 5,000 km as well as lower-altitude configurations, so it should not be described as exclusively LEO. Data-dependent tasks are explicitly left to future work. Good results relative to comparison algorithms do not establish a global optimum for arbitrary dynamic instances. [Table 3](../pdfs/dynamic-delay-sensitive-offloading.pdf#page=15){target="_blank" rel="noopener noreferrer"}; [conclusion](../pdfs/dynamic-delay-sensitive-offloading.pdf#page=24){target="_blank" rel="noopener noreferrer"}.

## Research connections and questions

*Follow-up interpretation:* compare neighbor-consensus costs with the time remaining before contact changes. How would dependent task graphs, delayed state updates, or unreliable ISLs alter the quality of insertion/removal decisions?

## Related papers in this library

- [Orbit-aware task scheduling in satellite edge computing](orbit-aware-task-scheduling.md)
- [Joint Task Offloading and Resource Allocation for LEO Satellite-Based Mobile Edge Computing Systems With Heterogeneous Task Demands](joint-offloading-heterogeneous-demands.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

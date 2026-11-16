---
title: "Orbital Edge Computing: Nanosatellite Constellations as a New Class of Computer System"
authors: "Bradley Denby; Brandon Lucia"
year: "2020"
tags:
  - LEO
  - Edge Computing
  - Systems
  - Earth Observation
  - Energy
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Orbital Edge Computing: Nanosatellite Constellations as a New Class of Computer System

**Authors:** Bradley Denby; Brandon Lucia  
**Year / version / venue:** ASPLOS 2020, March 16-20, Lausanne, Switzerland  
**Tags:** `LEO` `Edge Computing` `Systems` `Earth Observation` `Energy`

## Original paper

[Open supplied PDF](../pdfs/orbital-edge-computing-nanosatellites.pdf) · [DOI / preprint record](https://doi.org/10.1145/3373376.3378473)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

This paper proposes orbital edge computing as a computer-systems architecture for sensing nanosatellites. Rather than downlinking all raw imagery, satellites run local inference and retain information of interest. Computational nanosatellite pipelines coordinate sensing and processing through physical constellation geometry, reducing reliance on cross-link coordination. A runtime models orbital position, ground contact, and energy availability. [Abstract](../pdfs/orbital-edge-computing-nanosatellites.pdf#page=1).

## Research problem

A bent-pipe design becomes constrained by antenna capabilities, contact windows, ground-station contention, and harvested energy as the constellation grows. More satellites do not automatically produce proportionally more useful delivered data. The system therefore needs to co-design sensing, compute, communication, and physical deployment. [Sections 3-4](../pdfs/orbital-edge-computing-nanosatellites.pdf#page=3).

## Core approach

The paper explores four pipeline configurations: frame-spaced versus close-spaced placement, crossed with frame-parallel versus tile-parallel processing. Geographic progression determines which images or tiles each satellite processes. The system uses intelligent early discard to reduce downlink demand, and cote simulation/runtime tools model orbital and physical constraints. [Section 4.2 and Figure 5](../pdfs/orbital-edge-computing-nanosatellites.pdf#page=6).

## Evaluation and key results

The evaluation uses DetectNet building detection on SpaceNet imagery, measured inference power/latency on a Jetson TX2, and constellation simulations with 250 and 1,000 nanosatellites. Energy harvesting and storage are explicitly modeled. [Section 6](../pdfs/orbital-edge-computing-nanosatellites.pdf#page=9).

- In the evaluated setup, OEC reaches a low downlink-deficit plateau with **24 times fewer ground stations** than the bent-pipe configuration. This is not a blanket elimination of all communication deficits. [Figure 6](../pdfs/orbital-edge-computing-nanosatellites.pdf#page=10).
- Close-spaced tile-parallel pipelines deliver a reported **over 617-fold reduction in frame-processing latency** in the studied comparison. Frame-spaced placement does not give the same latency behavior. [Figure 7](../pdfs/orbital-edge-computing-nanosatellites.pdf#page=11).
- Increasing harvested power can improve coverage more than simply adding compute or energy storage at the examined design point. [Figure 8](../pdfs/orbital-edge-computing-nanosatellites.pdf#page=11).

## Limitations

The large performance factors depend on the selected constellation, ground-station arrangement, hardware, and application. Close-spaced formation flying has operational costs; feature filtering can discard information that a later task would need. The no-cross-link computational pipeline is a particular architecture, not a result that all distributed satellite workloads can avoid communication.

## Research connections and questions

*Follow-up interpretation:* treat physical arrangement as part of parallel-system design. Compare this geometry-driven pipeline with later ISL-connected, application-transparent orchestration such as Krios. Which workloads can exploit predictable repeated observations without transferring raw data between satellites?

## Related papers in this library

- [A comprehensive survey of orbital edge computing: Systems, applications, and algorithms](survey-orbital-edge-computing.md)
- [Krios: Scheduling Abstractions and Mechanisms for Enabling a LEO Compute Cloud](krios-leo-compute-cloud.md)
- [Semantic and goal-oriented edge computing for satellite Earth Observation](semantic-goal-oriented-earth-observation.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

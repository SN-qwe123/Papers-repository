---
title: "Edge Intelligence for Satellite-based Earth Observation: Scheduling Image Acquisition and Processing"
authors: "Beatriz Soret; Antonio M. Mercado-Martínez; Antonio Jurado-Navas; Nicolai D. Lyholm; Marco Moretti; Petar Popovski; Israel Leyva-Mayorga"
year: "2026"
tags:
  - LEO
  - Earth Observation
  - ML
  - Scheduling
  - Energy
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Edge Intelligence for Satellite-based Earth Observation: Scheduling Image Acquisition and Processing

**Authors:** Beatriz Soret; Antonio M. Mercado-Martínez; Antonio Jurado-Navas; Nicolai D. Lyholm; Marco Moretti; Petar Popovski; Israel Leyva-Mayorga  
**Year / version / venue:** Supplied draft dated April 8, 2026; arXiv:2604.05937v1, posted April 7, 2026  
**Tags:** `LEO` `Earth Observation` `ML` `Scheduling` `Energy`

## Original paper

[Open supplied PDF](../pdfs/edge-intelligence-earth-observation.pdf) · [DOI / preprint record](https://arxiv.org/abs/2604.05937)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

This work connects two decisions that are often studied separately: when an agile Earth-observation satellite should acquire useful images, and where those images should be processed. Observation scheduling accounts for viewing geometry, atmospheric turbulence, attitude maneuvers, and energy. Processing scheduling allocates image workloads and clock frequencies across heterogeneous satellite and ground resources. Vessel detection with YOLOv8 provides the running application. The supplied version is explicitly marked **Draft**. [Abstract](../pdfs/edge-intelligence-earth-observation.pdf#page=1).

## Core approach

- **Observation layer:** a binary integer program maximizes observation profit, using a ground-sampling-distance-based quality measure subject to observation windows, attitude-transition feasibility, and maneuver-energy limits. The implementation uses SCIP.
- **Edge layer:** an image pipeline scatters data during slot k, processes it during k+1, and gathers results during k+2. It jointly chooses processing fractions and processor frequencies to minimize communication plus computation energy.
- **Hardware characterization:** measured GPU execution times inform a bulk-synchronous parallel model. The processing problem is reduced to a convex formulation after deriving the frequency choice for fixed allocation. [Sections 4.1-4.2](../pdfs/edge-intelligence-earth-observation.pdf#page=13); [convex reduction](../pdfs/edge-intelligence-earth-observation.pdf#page=15).

## Evaluation

The example system uses 23 edge satellites supporting one EO satellite, WorldView-3-inspired acquisition parameters, 617 km altitude, and heterogeneous CPU/GPU configurations. The observation study compares against FIFO and a genetic algorithm. Table 3 gives communication, energy, and hardware settings; later experiments use 26 KSAT ground stations. [Sections 5-5.1 and Table 3](../pdfs/edge-intelligence-earth-observation.pdf#page=15).

## Key results

- In the turbulence-aware multi-target evaluation, successful observation rates range from **84.5% to 90%**. Targets need about **1.5 attempts on average**, showing that rescheduling does not make acquisition failure disappear. [Table 4](../pdfs/edge-intelligence-earth-observation.pdf#page=18).
- For the fixed-topology workload comparison, AGX GPU processing is reported as almost **30 times as power-efficient** as the modeled satellite CPU. In the orbital scenario, Nano Super energy per observation is more than five times that of AGX. These are configuration-specific comparisons. [Figures 10-11 and discussion](../pdfs/edge-intelligence-earth-observation.pdf#page=20).
- Batch execution-time quantiles are close to the mean in the tested operating range, supporting the chosen pipeline timing approximation. [Equations 28-29 and Figure 9](../pdfs/edge-intelligence-earth-observation.pdf#page=20).

## Limitations

The observation and processing problems are coupled through a staged workflow, rather than solved as one unrestricted joint optimization. The evaluation uses a specific geometry, hardware models, detector, and workload. Dense-object images can produce bimodal inference-time behavior, noted by the authors, which complicates simple distribution fits. Storage constraints are omitted from the observation formulation under its processing assumptions. [Pages 12-13](../pdfs/edge-intelligence-earth-observation.pdf#page=12); [execution-time discussion](../pdfs/edge-intelligence-earth-observation.pdf#page=18).

## Research connections and questions

*Follow-up interpretation:* combine acquisition-quality scheduling with explicit tail-latency constraints. What changes if image arrivals overlap, queues accumulate, or GPU execution distributions drift over time?

## Related papers in this library

- [Semantic and goal-oriented edge computing for satellite Earth Observation](semantic-goal-oriented-earth-observation.md)
- [Statistical Analysis for Energy-Efficient Satellite Edge Computing with Latency Guarantees](statistical-energy-latency-guarantees.md)
- [Orbit-aware task scheduling in satellite edge computing](orbit-aware-task-scheduling.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

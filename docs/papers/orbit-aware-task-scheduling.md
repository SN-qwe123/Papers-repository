---
title: "Orbit-aware task scheduling in satellite edge computing"
authors: "Danilo Magliarisi; Emiliano Casalicchio; Vincenzo Salvatore"
year: "2025"
tags:
  - LEO
  - Scheduling
  - Offloading
  - Distributed Systems
  - Real-Time
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Orbit-aware task scheduling in satellite edge computing

**Authors:** Danilo Magliarisi; Emiliano Casalicchio; Vincenzo Salvatore  
**Year / version / venue:** Cluster Computing, 28, article 1013  
**Tags:** `LEO` `Scheduling` `Offloading` `Distributed Systems` `Real-Time`

## Original paper

[Open supplied PDF](../pdfs/orbit-aware-task-scheduling.pdf){target="_blank" rel="noopener noreferrer"} · [DOI / preprint record](https://doi.org/10.1007/s10586-025-05663-9)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

This paper studies decentralized scheduling of long-running tasks on moving satellite edge nodes. It models a ground observer's listening dome and satellites' remaining visibility, then combines access-point selection, distributed task assignment, and queue management. The OrbitAware policy extends DTS-TMAX by checking whether predicted completion fits within remaining visibility. Here, **orbital sunset means leaving the observer's visibility region**, not entering Earth's shadow. [Abstract](../pdfs/orbit-aware-task-scheduling.pdf#page=1){target="_blank" rel="noopener noreferrer"}; [Section 5.3](../pdfs/orbit-aware-task-scheduling.pdf#page=10){target="_blank" rel="noopener noreferrer"}.

## Core approach

- Select nearby access satellites that are approaching the ground user, then distribute requests among those access points.
- Monitor neighboring nodes' resources and queued workloads to estimate response time.
- DTS-TMAX searches for feasible nodes under task deadlines and resource constraints; OrbitAware additionally compares estimated response time with time to orbital sunset.
- Dynamically adjust task priorities to reduce low-priority starvation. [Sections 5.1-5.4](../pdfs/orbit-aware-task-scheduling.pdf#page=8){target="_blank" rel="noopener noreferrer"}.

## Evaluation

The discrete-event study runs for 600 seconds. Table 2 uses exponential interarrival times with means of 0.5, 1, and 1.5 seconds; exponential service-time means of 10-50 seconds; a 30-second deadline; five access points; and 23 satellites in the listening dome. The initial priority mix is 20% high and 80% low. The orbital model permits more flexible neighborhood connectivity than a fixed four-neighbor grid. [Table 2](../pdfs/orbit-aware-task-scheduling.pdf#page=12){target="_blank" rel="noopener noreferrer"}.

## Key results

**The results do not show universal superiority of OrbitAware over DTS-TMAX.** Under the stationary evaluated conditions, the two policies behave similarly because their shared access-point selection already favors satellites with long remaining visibility. The paper explains that scenarios in which OrbitAware would gain more from overload lie outside those model assumptions. [Section 7.2](../pdfs/orbit-aware-task-scheduling.pdf#page=14){target="_blank" rel="noopener noreferrer"}.

The conclusion reports fewer than 15% of requests executed after sunset for OrbitAware in the study, but deadline violations can remain substantial when mean service time exceeds the 30-second deadline. Table 4 includes a **42.35% deadline-violation case**. Dynamic priority management improves successful completions and reduces mean response time by about two seconds in its reported comparison. [Tables 3-4](../pdfs/orbit-aware-task-scheduling.pdf#page=14){target="_blank" rel="noopener noreferrer"}; [Section 7.3 and conclusion](../pdfs/orbit-aware-task-scheduling.pdf#page=16){target="_blank" rel="noopener noreferrer"}.

## Limitations

Estimated feasibility does not guarantee every task meets its realized deadline. Outcomes depend on arrival/service distributions, the stationary operating regime, access-point selection, and visibility assumptions. Returning results after a node leaves the user's visible region is identified as future routing work. [Sections 7-8](../pdfs/orbit-aware-task-scheduling.pdf#page=14){target="_blank" rel="noopener noreferrer"}.

## Research connections and questions

*Follow-up interpretation:* compare orbit-aware placement with migration or result rerouting rather than treating visibility exit as the only outcome. Tail-aware response-time estimates may be more useful than means for admission control near a visibility deadline.

## Related papers in this library

- [Dynamic Delay-Sensitive Observation-Data-Processing Task Offloading for Satellite Edge Computing: A Fully-Decentralized Approach](dynamic-delay-sensitive-offloading.md)
- [Krios: Scheduling Abstractions and Mechanisms for Enabling a LEO Compute Cloud](krios-leo-compute-cloud.md)
- [Statistical Analysis for Energy-Efficient Satellite Edge Computing with Latency Guarantees](statistical-energy-latency-guarantees.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

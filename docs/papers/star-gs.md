---
title: "STAR-GS: Truthful and Visibility-Aware Resource Scheduling for Ground Station as a Service"
authors: "Zhiying Wang; Xiaojian Wang; Huayue Gu; Zhishan Guo; Ruozhou Yu"
year: "2026"
tags:
  - LEO
  - Real-Time
  - Scheduling
  - GSaaS
  - Mechanism Design
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# STAR-GS: Truthful and Visibility-Aware Resource Scheduling for Ground Station as a Service

**Authors:** Zhiying Wang; Xiaojian Wang; Huayue Gu; Zhishan Guo; Ruozhou Yu  
**Year / version / venue:** Supplied manuscript with a 2026 IEEE copyright line. The filename mentions ICNP 2026; publication status and venue are not independently established by these notes.  
**Tags:** `LEO` `Real-Time` `Scheduling` `GSaaS` `Mechanism Design`

## Original paper

[Open supplied PDF](../pdfs/star-gs.pdf){target="_blank" rel="noopener noreferrer"}

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Results have not been independently reproduced. Research questions are suggestions, not the authors' conclusions or JustinN's personal judgments. Source links use PDF viewer page numbers.

## Summary

STAR-GS studies ground-station scheduling from the perspective of a commercial Ground Station as a Service (GSaaS) provider. It jointly considers which downlink requests to admit, where to serve them, how to allocate bandwidth before deadlines, and what to charge. The proposed mechanism combines bid-ordered admission, best-fit station assignment, Earliest Deadline First (EDF) feasibility checks, and critical-payment pricing. STK-driven simulations evaluate revenue, acceptance, and runtime under limited contact opportunities. [Source: abstract and introduction](../pdfs/star-gs.pdf#page=1){target="_blank" rel="noopener noreferrer"}.

## Research problem and model

Each request declares an arrival time, deadline, known data volume, and bid per unit of data. Service is available only where a task's lifetime intersects satellite–ground visibility windows. Multiple satellites share a station's capacity, but each task is assigned to at most one primary ground station; separate tasks from the same satellite may use different stations. A task pays only if its complete data volume is delivered before its deadline. [Source: system model](../pdfs/star-gs.pdf#page=3){target="_blank" rel="noopener noreferrer"}.

If a completed task has volume τ and unit price p, its payment is pτ. The provider's reserve unit price ρ imposes a minimum acceptable price. The objective maximizes total payment revenue; it should be distinguished from provider utility after subtracting reserve costs. The paper proves the general revenue-optimization problem NP-hard through a knapsack reduction. [Source: pricing and objective](../pdfs/star-gs.pdf#page=4){target="_blank" rel="noopener noreferrer"}.

## Core approach

1. **Convert bandwidth into processing time:** for a fixed station, normalize task volume by station bandwidth, effective spectral efficiency, and slot duration. Fractional bandwidth allocation becomes preemptive full-bandwidth time sharing for feasibility analysis.
2. **Check deadline feasibility:** simulate EDF service within the available contact slots and reject an admission when the resulting schedule cannot complete the candidate task set.
3. **Choose a station:** process tasks in descending unit-bid order. Among feasible station assignments, choose the station with the smallest residual slack to preserve other capacity for later requests.
4. **Admit feasible requests:** skip bids below the reserve price; tentatively add each remaining request and rerun assignment/feasibility checks.
5. **Compute payments:** for every winner, search candidate bid thresholds while holding other bids fixed and rerunning selection, charging the critical winning price rather than automatically charging its submitted bid.

[Source: bandwidth–scheduling transformation](../pdfs/star-gs.pdf#page=5){target="_blank" rel="noopener noreferrer"}; [Source: assignment, admission, and pricing algorithms](../pdfs/star-gs.pdf#page=7){target="_blank" rel="noopener noreferrer"}.

## Claimed theoretical properties

The manuscript states dominant-strategy incentive compatibility, individual rationality, reserve-price protection, and polynomial runtime. These claims use a **single-parameter private-value model**: only valuation is private, while demand, deadlines, visibility, station capacity, and channel rates are public or verifiable. They should not be interpreted as protection against falsified task sizes, deadlines, or contact information. The notes summarize the claims without independently validating all proofs. [Source: theoretical analysis](../pdfs/star-gs.pdf#page=8){target="_blank" rel="noopener noreferrer"}.

## Evaluation setup

The discrete-time simulator uses STK-generated access windows for **24 satellites in three orbital planes and six ground stations**. Its default horizon is 24 hours in 60-second slots, with 300 requests, 5–20 GB demand, and deadline slack of 30–90 slots. Each experiment averages ten random seeds. [Source: setup and Table II](../pdfs/star-gs.pdf#page=9){target="_blank" rel="noopener noreferrer"}.

Comparisons include a small-instance **TSN-MILP** optimization benchmark, **CR-Throughput**, bid-agnostic **EDF**, **Highest-Bid-First with Naive Assignment (HBF-NA)**, and **Satellite-Centric Best-Visibility (SC-BV)**. Parameter sweeps cover task count, bandwidth, deadline slack, demand, and bid dispersion. [Source: baseline definitions](../pdfs/star-gs.pdf#page=9){target="_blank" rel="noopener noreferrer"}.

## Key results

- At **500 tasks**, the reported revenues of EDF, HBF-NA, and SC-BV are approximately **76.8%, 51.0%, and 22.4%** of STAR-GS revenue, respectively, in the overall comparison.
- STAR-GS maintains an acceptance ratio close to EDF while favoring higher-value feasible requests.
- On **30–270 tasks**, STAR-GS is close to TSN-MILP **when both are evaluated using submitted-bid pricing**. The separate critical-pricing curve yields lower actual payments, reflecting the cost of the truthful payment mechanism.
- TSN-MILP runtime exceeds **32 seconds at 270 tasks**. STAR-GS is around five seconds near this scale and approximately **20 seconds at 900 tasks** in the reported simulation.

[Source: overall comparisons](../pdfs/star-gs.pdf#page=9){target="_blank" rel="noopener noreferrer"}; [Source: pricing distinction and runtime, Fig. 3](../pdfs/star-gs.pdf#page=10){target="_blank" rel="noopener noreferrer"}.

## Limitations and reading cautions

“Near-MILP revenue” refers to the bid-priced allocation comparison, not equality between truthful critical-payment revenue and the MILP bid-price objective. The mechanism is a heuristic for the NP-hard scheduling/assignment problem; the experiments do not establish global optimality. Feasibility and incentive claims depend on the stated model and implementation assumptions.

The model uses a finite planning horizon, fixed effective link efficiencies, known task volumes, and one primary station per task. The authors identify online arrivals, time-varying channels, dynamic station capacity, adaptive reserves, and multi-station task splitting as future work. The evaluation is simulation-based. [Source: system assumptions](../pdfs/star-gs.pdf#page=4){target="_blank" rel="noopener noreferrer"}; [Source: conclusion and future work](../pdfs/star-gs.pdf#page=10){target="_blank" rel="noopener noreferrer"}.

## Research connections and questions

*Suggested follow-up:* evaluate robustness when contact windows or transmission rates are uncertain. How do critical-price computations scale when requests arrive continuously? What changes to allocation monotonicity and pricing are needed if one task can span multiple stations or users can misreport multiple task attributes?

## Related papers in this library

- [AdaOrb](adaorb.md): schedules downlink training data to improve future analytics accuracy, rather than provider revenue.
- [OrbitChain](orbitchain.md): reduces dependence on ground downloads by processing analytics across satellites.


## Personal notes

<!-- Add JustinN's own observations, annotations, and follow-up experiments here. -->

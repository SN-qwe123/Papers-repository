---
title: "Statistical Analysis for Energy-Efficient Satellite Edge Computing with Latency Guarantees"
authors: "Nicolai Dalsgaard Lyholm; Beatriz Soret; Tijana Devaja; Thomas Gundgaard Mulvad; Cedomir Stefanovic; Israel Leyva-Mayorga"
year: "2026"
tags:
  - LEO
  - Real-Time
  - Energy
  - ML
  - Statistical Modeling
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Statistical Analysis for Energy-Efficient Satellite Edge Computing with Latency Guarantees

**Authors:** Nicolai Dalsgaard Lyholm; Beatriz Soret; Tijana Devaja; Thomas Gundgaard Mulvad; Cedomir Stefanovic; Israel Leyva-Mayorga  
**Year / version / venue:** Supplied arXiv preprint, arXiv:2605.10215v1, May 11, 2026  
**Tags:** `LEO` `Real-Time` `Energy` `ML` `Statistical Modeling`

## Original paper

[Open supplied PDF](../pdfs/statistical-energy-latency-guarantees.pdf){target="_blank" rel="noopener noreferrer"} · [DOI / preprint record](https://arxiv.org/abs/2605.10215)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

This paper chooses a satellite GPU operating frequency using an execution-time distribution rather than only an average or a distribution-free bound. It fits frequency-dependent Gamma distributions to YOLOv8m inference measurements and combines processing time with an end-to-end communication budget. The goal is to minimize energy while satisfying a specified probability of timely completion. It also investigates how limited characterization data can undermine that probability. [Abstract](../pdfs/statistical-energy-latency-guarantees.pdf#page=1){target="_blank" rel="noopener noreferrer"}.

## Model and method

The end-to-end budget includes uplink, inter-satellite, processing, and downlink delays. A bulk-synchronous parallel model describes mean execution time, with cubic frequency scaling for power. Gamma shape and scale parameters are fitted as functions of frequency. Under the independent, identically distributed per-image assumption, batch execution time is also Gamma distributed. The chosen frequency is the minimum satisfying the processing-time cumulative-probability constraint. [Equations 7-17](../pdfs/statistical-energy-latency-guarantees.pdf#page=3){target="_blank" rel="noopener noreferrer"}.

The comparison method uses a Chebyshev-Cantelli bound based on the first two moments. Subsampling experiments evaluate how uncertain parameter estimates affect frequency selection and deadline misses. [Sections II.E-II.F](../pdfs/statistical-energy-latency-guarantees.pdf#page=3){target="_blank" rel="noopener noreferrer"}.

## Evaluation and key results

The evaluation uses **YOLOv8m**, the **56-image Ships-Google-Earth dataset**, and NVIDIA Jetson Orin Nano and AGX Orin platforms. Each image is executed 1,000 times per available frequency for the reference characterization. Default targets are **95% reliability** and a **500 ms end-to-end deadline**. [Experimental setup](../pdfs/statistical-energy-latency-guarantees.pdf#page=4){target="_blank" rel="noopener noreferrer"}.

- The authors report **more than 50% lower processing energy** than the Cantelli baseline while meeting the modeled target. This comparison concerns processing energy, not every component of spacecraft energy. [Conclusion](../pdfs/statistical-energy-latency-guarantees.pdf#page=6){target="_blank" rel="noopener noreferrer"}.
- Small fitting samples underestimate the execution-time tail in the reported experiments. Around **1,000 samples**, miss probability stabilizes near the 5% target. [Figure 3](../pdfs/statistical-energy-latency-guarantees.pdf#page=5){target="_blank" rel="noopener noreferrer"}.
- Tighter communication conditions consume the processing budget, forcing higher frequencies and eventually making requests infeasible regardless of the processing strategy. [Figures 4-5](../pdfs/statistical-energy-latency-guarantees.pdf#page=5){target="_blank" rel="noopener noreferrer"}.

## Limitations and verification notes

These are probabilistic, model-dependent guarantees, not hard real-time worst-case guarantees. Independence, Gamma fit quality, workload stability, and power-model validity matter. The energy comparison emphasizes high-elevation, negligible-retransmission conditions before exploring elevation effects. The PDF uses shortened or inconsistent Nano device labels in places; the experimental setup, Table I, and conclusion identify the Orin Nano/AGX family. [Pages 4-6](../pdfs/statistical-energy-latency-guarantees.pdf#page=4){target="_blank" rel="noopener noreferrer"}.

## Research connections and questions

*Follow-up interpretation:* extend deadline feasibility checks with measured tail distributions. How should a scheduler detect model drift, budget uncertainty across communication and compute, or reject requests when its statistical evidence is insufficient?

## Related papers in this library

- [Edge Intelligence for Satellite-based Earth Observation: Scheduling Image Acquisition and Processing](edge-intelligence-earth-observation.md)
- [Orbit-aware task scheduling in satellite edge computing](orbit-aware-task-scheduling.md)
- [Joint Task Offloading and Resource Allocation for LEO Satellite-Based Mobile Edge Computing Systems With Heterogeneous Task Demands](joint-offloading-heterogeneous-demands.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

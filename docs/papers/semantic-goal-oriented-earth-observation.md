---
title: "Semantic and goal-oriented edge computing for satellite Earth Observation"
authors: "Beatriz Soret; Israel Leyva-Mayorga; Antonio M. Mercado-Martínez; Marco Moretti; Antonio Jurado-Navas; Marc Martinez-Gost; Celia Sánchez de Miguel; Ainoa Salas-Prendes; Petar Popovski"
year: "2024"
tags:
  - LEO
  - Earth Observation
  - Semantic Communications
  - ML
  - Energy
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Semantic and goal-oriented edge computing for satellite Earth Observation

**Authors:** Beatriz Soret; Israel Leyva-Mayorga; Antonio M. Mercado-Martínez; Marco Moretti; Antonio Jurado-Navas; Marc Martinez-Gost; Celia Sánchez de Miguel; Ainoa Salas-Prendes; Petar Popovski  
**Year / version / venue:** Supplied arXiv preprint, arXiv:2408.15639v1, August 28, 2024  
**Tags:** `LEO` `Earth Observation` `Semantic Communications` `ML` `Energy`

## Original paper

[Open supplied PDF](../pdfs/semantic-goal-oriented-earth-observation.pdf){target="_blank" rel="noopener noreferrer"} · [DOI / preprint record](https://arxiv.org/abs/2408.15639)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

This paper frames satellite Earth observation around the information needed for a task rather than the delivery of all captured pixels. A LEO edge layer performs semantic extraction and sends compact outputs to the ground. The architecture connects observation, distributed processing, communication, and possible follow-up queries. Vessel detection illustrates the tradeoff among energy, latency, and task quality. [Abstract and introduction](../pdfs/semantic-goal-oriented-earth-observation.pdf#page=1){target="_blank" rel="noopener noreferrer"}.

## Core approach

The authors distinguish image reconstruction, object detection/localization, and closed-loop tracking as progressively richer task objectives. EO satellites acquire and distribute data; edge satellites extract semantics; the ground station aggregates and interprets results. Unprocessed raw data can fall back to ground processing when edge resources are insufficient. [Architecture and procedure](../pdfs/semantic-goal-oriented-earth-observation.pdf#page=4){target="_blank" rel="noopener noreferrer"}.

Optimization should track task-achievement metrics, timing/queue stability, and energy together. For example, detector recall is more directly tied to vessel detection than reconstruction error alone. Processing increases compute energy but reduces transmitted data, so maximum onboard processing is not automatically the energy optimum. [Metrics and tradeoffs](../pdfs/semantic-goal-oriented-earth-observation.pdf#page=5){target="_blank" rel="noopener noreferrer"}.

## Evaluation and key results

The illustrative system includes **23 edge satellites**, optical ISLs, an RF feeder link, and WorldView-3-inspired imagery. Images are 600 by 600 pixels at 0.5 m GSD. YOLOv8 ship detection is modeled at 79.1 GFLOPs per image, with average semantic output of **336 bits per image**. Satellite and ground CPU/GPU options are compared. [Section V](../pdfs/semantic-goal-oriented-earth-observation.pdf#page=6){target="_blank" rel="noopener noreferrer"}.

Figure 4 shows that lower-load CPU operation can be more power-efficient when CPU frequency is adjustable while GPUs run at maximum frequency. As image rate grows, ground-CPU-only processing becomes unattractive, and mixed edge/ground execution is needed for the modeled optimum. The result is conditional on the paper's frequency-control and hardware assumptions, not a general claim that CPUs outperform GPUs. [Figure 4 discussion](../pdfs/semantic-goal-oriented-earth-observation.pdf#page=6){target="_blank" rel="noopener noreferrer"}.

## Limitations

The evaluation is an illustrative modeled scenario, not a deployed closed-loop tracking system. The detector, image statistics, processing models, and semantic message definition determine the result. The closed-loop vision and broad optimization agenda go beyond what the numerical example demonstrates.

## Research connections and questions

*Follow-up interpretation:* quantify useful answers delivered before a deadline, not only bytes delivered. How should the system respond when detector confidence falls because of turbulence, or when a compact semantic output omits evidence needed for a later query?

## Related papers in this library

- [Edge Intelligence for Satellite-based Earth Observation: Scheduling Image Acquisition and Processing](edge-intelligence-earth-observation.md)
- [Statistical Analysis for Energy-Efficient Satellite Edge Computing with Latency Guarantees](statistical-energy-latency-guarantees.md)
- [Orbital Edge Computing: Nanosatellite Constellations as a New Class of Computer System](orbital-edge-computing-nanosatellites.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

---
title: "AdaOrb: Adapting In-Orbit Analytics Models for Location-aware Earth Observation Tasks"
authors: "Zhouyu Li; Pinxiang Wang; Xiaochun Liang; Xuanhao Luo; Yuchen Liu; Xiaojian Wang; Huayue Gu; Ruozhou Yu"
year: "Not specified"
tags:
  - LEO
  - ML
  - Edge Computing
  - Scheduling
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# AdaOrb: Adapting In-Orbit Analytics Models for Location-aware Earth Observation Tasks

**Authors:** Zhouyu Li; Pinxiang Wang; Xiaochun Liang; Xuanhao Luo; Yuchen Liu; Xiaojian Wang; Huayue Gu; Ruozhou Yu  
**Year / version / venue:** Supplied manuscript; publication year and venue are not specified in this copy.  
**Tags:** `LEO` `ML` `Edge Computing` `Scheduling`

## Original paper

[Open supplied PDF](../pdfs/adaorb.pdf){target="_blank" rel="noopener noreferrer"}

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Results have not been independently reproduced. Research questions are suggestions, not the authors' conclusions or JustinN's personal judgments. Source links use PDF viewer page numbers.

## Summary

AdaOrb adapts onboard Earth-observation models to the geographic areas where they will be used. Rather than retraining on the satellite, it schedules which newly captured images to download, retrains location-specific models on the ground, and uploads updated weights. A model predictive control (MPC) scheduler allocates scarce downlink capacity using predicted ground contacts, future observations, and an estimated relationship between training-data volume and model accuracy. The goal is better accuracy across the stream of future in-orbit predictions. [Source: abstract and introduction](../pdfs/adaorb.pdf#page=1){target="_blank" rel="noopener noreferrer"}.

## Research problem

Lightweight models trained for one region may perform poorly in another because of geographic and sensor-related distribution shifts. New user tasks can target previously unseen locations, while brief satellite–ground contacts prevent downloading all available training data. A purely immediate allocation can miss the chance to improve a model before a valuable upcoming observation. AdaOrb exploits predictable orbits and intervening ground contacts to plan those updates. The preliminary study uses cross-location building segmentation to motivate dedicated models and accumulated-data retraining. [Source: preliminary experiments](../pdfs/adaorb.pdf#page=2){target="_blank" rel="noopener noreferrer"}.

## Core approach

1. **Collect and predict:** track captured images, current model accuracy, upcoming area visits, and ground-contact capacities for each task.
2. **Profile adaptation:** fit an approximate accuracy-versus-training-data curve from offline retraining experiments. The evaluated implementation uses a fifth-degree polynomial fitted to the average curve from five locations.
3. **Plan downlinks:** MPC minimizes predicted error weighted by the number of future images, subject to contact capacity and the amount of data actually available. Replan as the task/model state changes.
4. **Update on the ground:** download selected images, annotate them, retrain with accumulated data, and upload weights during the next contact. Inference continues onboard.

The model explicitly includes a contact-to-contact delay before new training data improves onboard accuracy. It assumes enough ground-side annotation, training, and communication resources to complete the update in time. [Source: system design and optimization](../pdfs/adaorb.pdf#page=4){target="_blank" rel="noopener noreferrer"}; [Source: profiling and implementation](../pdfs/adaorb.pdf#page=5){target="_blank" rel="noopener noreferrer"}.

## Evaluation setup

- **Workload:** building segmentation using SpaceNet data; 54 SpaceNet 7 evaluation locations, excluding the five used for accuracy-function profiling.
- **Model:** a pruned UNet with approximately 63,000 parameters, pretrained using SpaceNet 1; retraining uses accumulated images with an 80/20 training/validation split, up to 20 epochs, and a cap of 300 retraining images per task.
- **Orbital traces:** one month of Hypatia traces for Sentinel-2 and Starlink scenarios. The nominal downlink is 125 Mbps, with 10% reserved for retraining data; model-upload capacity is assumed sufficient.
- **Comparisons:** Random allocation, Accuracy-based allocation favoring less accurate models, and Data-based allocation using predicted incoming image volume.
- **Metric:** cumulative utility sums DICE accuracy over the in-orbit predictions, so it reflects both accuracy and the number of predictions benefiting from each update.

[Source: evaluation methodology](../pdfs/adaorb.pdf#page=5){target="_blank" rel="noopener noreferrer"}.

## Key results

AdaOrb achieves higher cumulative utility than the compared allocation policies after an initial bootstrap period in the reported experiments. The prediction-horizon study shows that a longer horizon is not always better: planning too far ahead can become less useful as the task set changes. The default horizons are five ground contacts for Sentinel-2 and twenty for Starlink. [Source: performance and horizon studies](../pdfs/adaorb.pdf#page=6){target="_blank" rel="noopener noreferrer"}.

On the Jetson Orin Nano, median tile inference takes **11.9 ms with GPU acceleration**, compared with **58.5 ms on the CPU**. The ground-side MPC decision time has a median below three seconds in the reported desktop measurements, supporting its use between ground contacts. These are testbed measurements, not flight-deployment results. [Source: system overhead](../pdfs/adaorb.pdf#page=6){target="_blank" rel="noopener noreferrer"}.

## Limitations and reading cautions

The evaluated task is building segmentation; the accuracy function is profiled from a small set of locations and approximated across tasks. Generalization to other sensors, models, and tasks needs validation. Ground annotation/retraining turnaround and sufficient uplink are assumptions that can materially affect the update cycle. Predictable trajectories do not eliminate uncertainty in clouds, image usefulness, or future user requests. The comparison concerns the tested allocation policies, not every possible adaptive-learning scheduler.

## Research connections and questions

*Suggested follow-up:* combine adaptation value with explicit annotation latency, training cost, and uncertain contact capacity. How much utility is lost when the profiled accuracy curve is wrong? Could selecting informative images improve the value of each downloaded byte beyond selecting only image counts?

## Related papers in this library

- [OrbitChain](orbitchain.md): allocates in-orbit compute and routes analytics pipelines; AdaOrb focuses on keeping their models accurate.
- [STAR-GS](star-gs.md): allocates ground-station downlink service under deadlines and pricing constraints.
- [Orbital Edge Computing: Nanosatellite Constellations as a New Class of Computer System](orbital-edge-computing-nanosatellites.md): background on constellation-scale computation.

## Personal notes

<!-- Add JustinN's own observations, annotations, and follow-up experiments here. -->

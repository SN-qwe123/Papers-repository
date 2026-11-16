---
title: "Krios: Scheduling Abstractions and Mechanisms for Enabling a LEO Compute Cloud"
authors: "Vaibhav Bhosale; Ada Gavrilovska; Ketan Bhardwaj"
year: "2024"
tags:
  - LEO
  - Scheduling
  - Cloud
  - Systems
  - Kubernetes
---

<!-- Library notes: JustinN | https://github.com/SN-qwe123/Papers-repository -->

[← Back to library](../index.md)

# Krios: Scheduling Abstractions and Mechanisms for Enabling a LEO Compute Cloud

**Authors:** Vaibhav Bhosale; Ada Gavrilovska; Ketan Bhardwaj  
**Year / version / venue:** ACM Symposium on Cloud Computing (SoCC 2024), November 20-22, Redmond, WA  
**Tags:** `LEO` `Scheduling` `Cloud` `Systems` `Kubernetes`

## Original paper

[Open supplied PDF](../pdfs/krios-leo-compute-cloud.pdf) · [DOI / preprint record](https://doi.org/10.1145/3698038.3698566)

> **Note provenance:** AI-assisted reading notes prepared from the supplied PDF. Reported results have not been independently reproduced. Research questions below are suggestions, not the author's conclusions or JustinN's personal judgments. Page links use the PDF viewer's page numbering.

## Summary

Krios is an orchestration system for applications hosted on moving LEO satellites. Its key abstraction is a **LEO zone**: an application specifies the geographic region where it must be available, rather than a fixed physical cluster. Predictive scheduling and proactive application handovers then maintain that availability as satellites move. This addresses long-lived service placement, which differs from scheduling a one-shot computational task. [Abstract](../pdfs/krios-leo-compute-cloud.pdf#page=1); [LEO zones](../pdfs/krios-leo-compute-cloud.pdf#page=4).

## Core approach

1. Express a zone in application deployment metadata.
2. Use orbital information to identify satellites that can serve the region and prefer longer useful visibility.
3. Predict when the current satellite will leave and initialize a replacement before that event.
4. Remove the old instance only after the new one is running. A state handler and Krios-volume support local state movement where appropriate.

The zone manager evaluates functions on demand rather than continuously maintaining every zone's membership. The prototype extends Kubernetes, uses TLEs with an SGP4 path model, and is implemented as a Python package. [Sections 5.1-5.4](../pdfs/krios-leo-compute-cloud.pdf#page=6).

## Evaluation and key results

Experiments use a custom VM-based emulator, with satellite identities and link delays changing over time. Runs span 100 minutes, covering about one orbit. Workloads include trail-map serving, oil-rig monitoring, and parameterized request/response services. Comparisons include stock Kubernetes, incremental mobility-aware baselines, broad application replication, and ground-station edge placement. [Section 6](../pdfs/krios-leo-compute-cloud.pdf#page=9).

For the national-park example, Krios provides comparable responsiveness to a **475-instance** replication deployment using approximately **one active application instance**, with temporary overlap for handovers. The reported median handover interval is approximately **200 seconds** for that zone. The abstract reports **6-10 times less frequent handovers** than comparison approaches. These numbers depend on zone geometry, orbit, and workload. [Abstract](../pdfs/krios-leo-compute-cloud.pdf#page=1); [Section 7.1](../pdfs/krios-leo-compute-cloud.pdf#page=11).

## Limitations

The prototype uses circular zones, with the evaluated design restricting zone radius to 100 km. Energy-aware orchestration and large-scale multi-application policies are future work. The emulator focuses on position-dependent latency and does not model all queueing effects. Large mutable state requires careful cost/correctness analysis; the state-transfer discussion does not establish transparent strong consistency for arbitrary applications. [Zone limits](../pdfs/krios-leo-compute-cloud.pdf#page=7); [methodology](../pdfs/krios-leo-compute-cloud.pdf#page=9); [discussion](../pdfs/krios-leo-compute-cloud.pdf#page=14).

## Research connections and questions

*Follow-up interpretation:* use predicted visibility as a scheduling event, not merely a static node property. How should a scheduler combine remaining visibility, migration cost, mutable state, and battery availability?

## Implementation resource

[Author-reported Krios repository](https://github.com/GTkernel/krios) — listed in Section 5.4 of the supplied PDF; not independently reproduced here.

## Related papers in this library

- [Orbit-aware task scheduling in satellite edge computing](orbit-aware-task-scheduling.md)
- [Orbital Edge Computing: Nanosatellite Constellations as a New Class of Computer System](orbital-edge-computing-nanosatellites.md)
- [LEO Satellite Networking Relaunched: Survey and Current Research Challenges](leo-networking-relaunched.md)

## Personal notes

<!-- Add your own assessment, reproduction notes, and questions here. -->

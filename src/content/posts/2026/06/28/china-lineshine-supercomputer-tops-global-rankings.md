---
story_id: story_952c27db
title: China's LineShine Supercomputer Retakes Global No. 1 Spot
date: '2026-06-28T05:18:00Z'
meta_description: China's LineShine supercomputer tops the TOP500 at 2.198 exaflops,
  the first CPU-only system past 2 exaflops and China's return to No. 1 after nine
  years.
slug: china-lineshine-supercomputer-tops-global-rankings
read_time_minutes: 5
word_count: 826
tags:
- supercomputing
- TOP500
- China
- LineShine
- exascale
categories:
- Science & Technology
style: formal_news
draft: false
---
# China's LineShine Supercomputer Tops Global Rankings at 2.198 Exaflops

China has reclaimed the world's fastest supercomputer crown with the debut of LineShine (Lingsheng), a domestically developed system that achieved 2.198 exaflops on the High Performance Linpack (HPL) benchmark, according to the [67th TOP500 list](https://www.top500.org/news/lineshine-debuts-no-1-top500-enters-new-global-exascale-era/) announced June 23 at the ISC 2026 High Performance Conference in Hamburg, Germany. The system, installed at the National Supercomputing Centre in Shenzhen (NSCS), displaces the U.S. Department of Energy's El Capitan and marks China's return to the No. 1 position for the first time since the Sunway TaihuLight in 2017.

## A CPU-Only Exascale Achievement

LineShine is the first system in TOP500 history to exceed two exaflops of sustained double-precision performance using only CPUs — without GPU accelerators. Built on the custom "LingKun" platform, the system packs 13.79 million cores across approximately 40,000 to 47,000 LX2 processors, each a 304-core chip based on the Armv9 instruction set running at 1.55 GHz.

The LX2 processor, believed to be co-designed by NSCS and Huawei, uses a chiplet design with two compute chiplets per CPU, organized into eight clusters of 38 cores each. Each core supports Arm's Scalable Vector Extension (SVE) and Scalable Matrix Extension (SME) for AI acceleration. The system achieves approximately 80% efficiency against its 2.736 exaflop/s theoretical peak.

According to the TOP500 organization, LineShine also took the No. 1 position on the HPCG benchmark — which measures real-world application performance — with 22.00 HPCG-Petaflop/s, ahead of El Capitan (17.41) and Japan's Fugaku (16.00).

## Full-Stack Domestic Technology

A defining feature of LineShine is its complete technological independence. As reported by [IT之家](https://www.ithome.com/0/944/839.htm), the system achieves full-stack independent controllability (软硬件全栈自主可控), with no reliance on foreign components. This includes the LX2 processors, the proprietary "LingQi" high-speed interconnect supporting up to 2 million ports, the Kylin operating system, and a 100% full liquid cooling system — the world's largest centralized liquid cooling installation.

"Lingsheng is the world's first supercomputer with sustained performance exceeding 2 Exaflops," said Lu Yutong, chief designer of the system and director of the National Supercomputing Center in Shenzhen, as quoted by IT之家.

Li Xiaoli, deputy director of the Shenzhen Science and Technology Innovation Bureau, described the achievement as "a landmark achievement in full-stack independent controllability in China's high-end computing field."

## Technical Specifications and Architecture

The system comprises 92 computer cabinets and 36 network cabinets, with total storage capacity of 650 PB. Power consumption is approximately 42.2 MW, yielding an energy efficiency of 52.07 Gigaflops/Watt — ranking No. 50 on the Green500 list. The 3D floating orthogonal architecture and centralized liquid cooling represent significant engineering innovations.

On the HPL-MxP mixed-precision benchmark, LineShine reached 7.92 Exaflop/s for fourth place, a comparatively modest 3.6x speedup over its HPL score. This reflects its CPU-only design without dedicated low-precision accelerators, contrasting with GPU-accelerated systems like El Capitan (9.2x speedup) and Aurora (11.5x speedup).

## A Reshuffled Global Top 10

LineShine's debut increases the number of exascale systems globally from four to five, placing exascale capability across Asia, North America, and Europe simultaneously. El Capitan (1.809 exaflops) drops to No. 2, followed by Frontier (1.353 exaflops) at No. 3, Aurora (1.012 exaflops) at No. 4, and Europe's JUPITER Booster (1.000 exaflops) at No. 5.

Italy's Eni S.p.A. enters the list with HPC7 at No. 6 (571.5 petaflops), while Microsoft's Azure-based Eagle system falls to No. 7 (561.2 petaflops). Japan's Fugaku holds No. 9 (442 petaflops), and Switzerland's Alps system rounds out the Top 10 (434.9 petaflops).

As [Network World](https://www.networkworld.com/article/4188115/chinas-lineshine-dethrones-el-capitan-as-the-worlds-fastest-supercomputer.html) reported, combined computing power across the entire TOP500 reached 18.74 exaflops, up from 14.99 exaflops six months ago, while accelerator adoption rose to 277 systems.

## Geopolitical and Strategic Significance

LineShine's achievement carries profound geopolitical weight. The system demonstrates China's ability to achieve world-leading high-performance computing performance despite U.S. export controls on advanced semiconductors and GPU technology. By achieving No. 1 with a CPU-only, fully domestic design, China signals technological self-sufficiency in a domain long dominated by U.S. and allied nations.

[TechRadar](https://www.techradar.com/pro/china-unveils-a-cpu-only-supercomputer-capable-of-1-54-exaflops-lineshine-lx2-packs-a-frankly-ridiculous-2-4-million-armv9-cores-from-huawei) noted that China is pursuing this CPU-only path largely due to U.S. bans on GPU exports, making a strategic trade-off: accepting lower performance density and higher power consumption in exchange for independence from foreign hardware ecosystems like Nvidia's CUDA platform.

## Scientific and Economic Impact

During the April 24 launch event at NSCS, researchers demonstrated applications across nine domains, including remote sensing, materials science, bioinformatics, meteorology, drug discovery, oil exploration, AI, life sciences, and electromagnetic simulation. Notable achievements include 1km-resolution global climate modeling, 100-million-atom materials simulations, and trillion-compound drug screening.

## What's Next

LineShine's debut opens new questions about the future trajectory of global supercomputing. Will the U.S. respond with accelerated investments or new export controls? Can China close the AI performance gap through software optimization? And how will LineShine's real-world scientific workloads compare to GPU-accelerated systems? What is clear is that the era of exascale computing has entered a new, multipolar phase — with custom Chinese silicon, AMD-based U.S. systems, and European sovereign computing infrastructure all competing at the highest level.
---
story_id: story_58bf1434
title: China's Ling Sheng Supercomputer Retakes World No. 1
date: '2026-07-11T08:30:00Z'
meta_description: China's Ling Sheng supercomputer tops the TOP500 list with 2.198
  EFLOPS, using a groundbreaking CPU-only architecture that bypasses US export controls.
slug: china-cpu-only-supercomputer-ling-sheng-world-no-1
read_time_minutes: 6
word_count: 1164
tags:
- supercomputing
- China
- TOP500
- Ling Sheng
- high-performance computing
categories:
- Technology
- Science
style: formal_news
draft: false
---
# China's Ling Sheng Supercomputer Retakes World No. 1

China has reclaimed the world's fastest supercomputer crown with the debut of **Ling Sheng** (also known internationally as LineShine), a domestically built system that achieved a sustained performance of **2.198 exaflops** — more than 2 quintillion calculations per second — at the International Supercomputing Conference (ISC 2026) in Hamburg, Germany, on June 23. The system, installed at the National Supercomputing Center Shenzhen (NSCS) in Guangming Science City, marks China's return to the top of the global TOP500 rankings for the first time since 2017, when the Sunway TaihuLight held the No. 1 position, according to [Xinhua News](https://www.news.cn/tech/20260711/258f3c194e50403a9173de9fee5188f8/c.html).

What makes Ling Sheng's achievement particularly significant is its architectural approach: the system uses a **purely CPU-based design** with no graphics processing units (GPUs) or external accelerators, breaking from the dominant CPU-GPU heterogeneous model used by virtually all other top-tier supercomputers. The system's LX2 processor, based on the ARMv9 architecture, integrates matrix acceleration computing units directly into the CPU, eliminating the need for separate GPU chips.

## A Deliberate Return to the Top

Ling Sheng's debut on the TOP500 list after years of Chinese systems staying off the rankings is widely seen as a deliberate strategic move. As [Tom's Hardware](https://www.tomshardware.com/tech-industry/supercomputers/china-tops-the-top500-with-a-cpu-only-supercomputer-ending-el-capitans-reign) noted, "the fact that a sanctioned country has managed to build an exascale flagship without a single Western accelerator is one thing, but what's more telling is that China has decided to put it on the list." Analyst Addison Snell of Intersect360 Research echoed this sentiment in the [New York Times](https://cn.nytimes.com/technology/20260624/china-supercomputer-crown-us/), stating: "That China has a system capable of winning doesn't surprise me; what surprises me is that they wanted the recognition."

The system displaced the U.S. Department of Energy's El Capitan supercomputer at Lawrence Livermore National Laboratory in California, which now sits at No. 2 with 1.809 EFLOPS — more than 20% slower than Ling Sheng. Other U.S. systems, Frontier (1.353 EFLOPS) and Aurora, occupy the No. 3 and No. 4 positions, while Germany's Jupiter rounds out the top five.

## Technical Breakthrough: The CPU-Only Architecture

Ling Sheng's most distinguishing feature is its rejection of the conventional supercomputing design paradigm. Most high-performance systems — including El Capitan, Frontier, and Aurora — rely on a hybrid architecture where CPUs handle general tasks while thousands of GPUs (typically from NVIDIA or AMD) perform the heavy parallel computation.

Ling Sheng takes a fundamentally different path. Its LX2 processor, designed in China and manufactured at an undisclosed process node, packs **304 cores running at 1.55 GHz** based on the ARMv9 instruction set architecture licensed from Arm Holdings. Across 20,480 compute nodes, the system totals approximately **13.79 million cores**, connected by a proprietary "LingQi" interconnect capable of 1.6 Tbps per node. The system runs on the domestic Kylin operating system and consumes approximately **42.2 megawatts** of power.

Prof. Lu Yutong, Chief Designer of Ling Sheng and Director of the National Supercomputing Center Shenzhen, explained the design philosophy in an article published by People's Daily: "The 'Ling Sheng' being able to reach the top is not about single-point performance breakthroughs, but about systematic innovation. It adopts full-stack domestic software and hardware, building an independently controllable systematic capability in key chips, high-speed interconnects, system software, green energy efficiency, and application coordination."

Jack Dongarra, a professor at the University of Tennessee and co-creator of the TOP500 benchmark, called the system "impressive" and noted: "They have surpassed us by developing a system that doesn't rely on GPUs." Dongarra also suggested that the underlying design "may point to a new path for better integrating AI with traditional scientific tasks."

## Geopolitical Implications: Bypassing Export Controls

The achievement carries significant geopolitical weight. The United States under the Trump administration has imposed tariffs and export restrictions on advanced AI chips to China, particularly targeting NVIDIA and AMD GPUs used in high-performance computing. Ling Sheng's CPU-only architecture effectively bypasses these restrictions.

Jimmy Goodrich, a senior researcher at UC San Diego's Institute for Global Conflict and Cooperation, told the New York Times: "The U.S. government should impose stricter controls on CPU exports and manufacturing for the Chinese market — this is a loophole in the current regulations."

The system uses China's first domestically produced High Bandwidth Memory (HBM), the LingQi interconnect, and the Kylin operating system — all developed within China. While the LX2 processor is based on ARM architecture licensed from the UK-based Arm Holdings (a SoftBank subsidiary), Arm confirmed it operates "in compliance with applicable export controls and regulations."

## Scientific and AI Applications

Despite its CPU-only design, Ling Sheng is not solely a traditional scientific computing machine. Prof. Lu described it as pioneering a "super-intelligence fusion architecture" that efficiently coordinates multiple computing modes, including both traditional supercomputing and AI workloads.

The system has already been deployed for applications including atmospheric and ocean modeling, engineering simulation, materials science, drug discovery, and large language model inference. It also ranks No. 1 on the HPCG benchmark (High Performance Conjugate Gradient) and No. 4 on the HPL-MxP mixed-precision benchmark, demonstrating strong performance across both traditional scientific and AI-oriented tasks.

However, experts caution that U.S. AI supercomputers using lower-precision computing may still lead in AI-specific workloads. As Goodrich noted, "China's achievement is noteworthy and impressive, but they cannot compare with the massive AI supercomputers being built by U.S. AI labs and others."

## A New Chapter in the Supercomputing Race

Ling Sheng's debut comes at a pivotal moment in the global supercomputing landscape. Only three nations currently operate publicly verified exascale-capable systems (exceeding 1 EFLOPS): China, the United States, and Germany. The TOP500 organization itself noted that Ling Sheng's success demonstrates "there is no single dominant technology path to leading-edge computing."

Historically, Chinese and Japanese systems topping the rankings have spurred increased U.S. government investment in supercomputing. The Trump administration's "Genesis Mission," launched in November 2025, aims to leverage U.S. national laboratory and private-sector supercomputers to boost AI and scientific research — an effort that may see accelerated funding in response to Ling Sheng's achievement.

For China, the return to No. 1 represents more than national pride. As Prof. Lu wrote: "Full-stack autonomy not only means safety and reliability, but also gives us the ability to master the initiative of supercomputing technology iteration and the right to define technical standards." With Ling Sheng, China has signaled that it can compete at the highest level of computing — and on its own terms.

## What to Watch For

Several open questions remain: Who manufactured the LX2 processor and at what process node? Was the system truly built without government funding, as Dongarra was told during his visit? How will the U.S. respond in terms of export control policy? And perhaps most importantly, will China continue to submit future systems to the TOP500 rankings, or was this a one-time statement of capability?

What is clear is that the global supercomputing race has entered a new phase — one defined not just by raw performance, but by architectural diversity, technological sovereignty, and the strategic calculus of when and how to reveal one's hand.
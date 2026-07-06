---
story_id: story_577c950b
title: Peking University Makes First Phase-Change Neuromorphic Chip
date: '2026-07-06T04:54:02Z'
meta_description: Peking University develops the world's first neuromorphic dynamics
  chip using phase-change memristors, achieving 2.12ms latency and 478x GPU speedup.
slug: peking-university-neuromorphic-chip-phase-change-memristors
read_time_minutes: 6
word_count: 1017
tags:
- neuromorphic computing
- phase-change memristors
- brain-computer interface
- Peking University
- AI hardware
- China
categories:
- Science
- Technology
style: formal_news
draft: false
---
# Peking University Makes First Phase-Change Neuromorphic Chip

A team from Peking University's School of Integrated Circuits, in collaboration with the Chinese Academy of Sciences, has developed the world's first neuromorphic dynamics system chip based on phase-change memristors — a breakthrough that compresses single-step computation latency to just 2.12 milliseconds and outperforms NVIDIA's A100 GPU by up to 478 times in brain cortex reconstruction tasks. The research was [published in the journal *Science*](https://ic.pku.edu.cn/xwdt/bda661dcd0154269a0fede1ab74e8306.htm) on July 3, 2026, marking a major milestone in overcoming a half-century bottleneck in real-time neuromorphic computing.

## The 50-Year Bottleneck

Neuromorphic dynamics systems combine neural networks with differential equations to model continuous physical processes — essential for real-time brain modeling, brain-computer interfaces (BCI), and medical imaging. Unlike standard neural networks that produce static outputs, these systems must model how brain states evolve over time.

However, traditional computer architecture has long struggled with this task. The Von Neumann architecture, which separates memory and processing, forces massive amounts of intermediate data to shuttle between memory and processor — a problem that has prevented real-time neuromorphic dynamics computation for 50 years. As [Guangming Daily reported](https://epaper.gmw.cn/gmrb/html/content/202607/04/content_18315.html), this creates prohibitive latency and power consumption that has kept these systems confined to offline, large-scale computing environments.

## A Paradigm Shift: Controllable In-Memory Computing

The Peking University team, led by Professor Yang Yuchao (杨玉超) and co-led by Researcher Song Zhitang (宋志棠) of the Shanghai Institute of Microsystem and Information Technology, turned a long-standing problem into an innovative solution.

Phase-change memory (PCM) materials can switch between amorphous and crystalline states, with different electrical resistance levels. The "conductance drift" phenomenon — where conductance changes predictably over time — was traditionally viewed as a defect. The team transformed this into a feature, using the predictable physical evolution of conductance states to perform computation directly in memory.

This new paradigm, called "controllable in-memory computing" (可控存内计算), integrates storage and computation at the physical level. Instead of using digital circuits to repeatedly read, write, compare, and compute, the chip lets the physical properties of the memory devices themselves perform the calculations. According to [People's Daily](http://edu.people.com.cn/n1/2026/0706/c1006-40754214.html), the approach eliminates the need for data movement between memory and processor — a bottleneck compared to an office worker constantly getting up to fetch files from a cabinet.

## Technical Specifications and Performance

Fabricated using a 40nm process, the chip's core compute array occupies just 0.28 mm². Operating at 50 MHz with a 9-stage pipeline for single-step integration, it achieves a single-step latency of 2.12 milliseconds — the first time neuromorphic dynamics hardware has entered the millisecond era.

The performance benchmarks are striking:

- **vs. State-of-the-art ASIC accelerators:** 3.82x to 36.27x speedup, with 11.75x to 24.73x lower power consumption
- **vs. NVIDIA A100 GPU (brain cortex reconstruction):** 50.38x to 478.18x speedup

"The performance is exhilarating," Professor Yang Yuchao told Guangming Daily, commenting on the benchmark results.

## Real-World Brain Reconstruction

The team demonstrated the chip's capabilities by using it for real-time reconstruction of brain white matter and gray matter cortex surfaces. The system generated smooth, closed, topologically consistent brain cortex surfaces that accurately captured complex folded structures while effectively suppressing artifacts and self-intersection defects common in traditional neural network methods.

"To enable machines to model and understand the physical world in real time like the human brain, we need a 'neuromorphic dynamics system' that combines neural networks with differential equations," Professor Yang explained. "It can reconstruct smooth and accurate 3D brain structures from incomplete, noisy data, with enormous application potential."

## Medical and BCI Applications

The breakthrough opens up transformative possibilities in medicine and brain-computer interfaces. The ability to reconstruct high-fidelity brain cortex surfaces in milliseconds rather than minutes or hours could revolutionize:

- **Intraoperative neural navigation** — Real-time brain mapping during surgery
- **Alzheimer's disease screening** — Early detection of structural brain changes
- **Brain digital twins** — Personalized, dynamic models of individual brains
- **BCI signal decoding** — Real-time interpretation of neural signals

Professor Yang noted that this breakthrough "opens up entirely new possibilities for brain-computer interfaces and the diagnosis and treatment of brain diseases," adding that personalized, dynamic brain digital twins will become possible with a hardware foundation that can run in real time.

*Science* magazine published a companion Perspective article alongside the research, praising it as representing "a paradigm shift toward physics-driven computing," according to the Peking University official announcement.

## Broader Context: China's BCI Industry

This breakthrough arrives at a pivotal moment for China's brain-computer interface industry. In March 2025, "brain-computer interfaces" were first written into China's Government Work Report as a future industry alongside quantum technology, embodied intelligence, and 6G. Multiple provinces have since issued BCI-specific policies.

China's BCI market was valued at approximately 3 billion RMB in 2025 and is projected to reach 12 billion RMB by 2030, according to the China Academy of Information and Communications Technology (CAICT). Globally, the BCI medical applications market is projected at $40 billion by 2030 and $145 billion by 2040, according to McKinsey.

## Geopolitical Significance

The achievement demonstrates China's growing capability in advanced semiconductor and AI hardware research, particularly in the "post-Moore era" where novel computing paradigms are increasingly important. Notably, the team achieved this breakthrough using a 40nm process node — relatively mature by global standards — showing that architectural and algorithmic innovation can compensate for process node disadvantages.

The research was supported by the New Cornerstone Investigator Program, the National Key R&D Program, the National Natural Science Foundation of China, and other major funding initiatives.

## What's Next

While the chip is currently a research prototype, its potential impact on the rapidly growing BCI and medical imaging markets is substantial. Key questions remain about the timeline for commercial production, manufacturing costs, and plans for scaling to more advanced process nodes. The team's success in turning a physical "defect" into a computational feature may inspire a new generation of physics-driven computing architectures.

As Professor Yang put it: "This breakthrough opens up entirely new possibilities." For a field that has waited half a century for real-time neuromorphic computing, those possibilities are now within reach.

---

*Image: The phase-change memristor-based millisecond neuromorphic dynamics system chip. (Credit: MyDrivers / 快科技)*

![Phase-change memristor neuromorphic dynamics system chip](https://img1.mydrivers.com/img/20260704/1bf7bff7-8b0f-43c7-b057-18d93360c07a.png)
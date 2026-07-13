---
story_id: story_49bc8e13
title: China's Lingsheng Supercomputer Reclaims World No. 1 Ranking
date: '2026-07-13T06:45:00Z'
meta_description: China's domestically-developed Lingsheng supercomputer tops the
  global TOP500 ranking with 2.198 EFLOPS, marking a return to No. 1 after nine years.
slug: china-lingsheng-supercomputer-reclaims-world-no-1
read_time_minutes: 5
word_count: 833
tags:
- supercomputing
- TOP500
- China
- HPC
- technology
categories:
- Technology
style: formal_news
draft: false
---
# China's Lingsheng Supercomputer Reclaims World No. 1 Ranking

China has returned to the top of the global supercomputing rankings for the first time in nearly a decade. The domestically-developed Lingsheng (灵晟) supercomputer, deployed at the National Supercomputing Center in Shenzhen, claimed the #1 spot on the 67th TOP500 list released June 23 at the International Supercomputing Conference (ISC 2026) in Hamburg, Germany. With a sustained performance of 2.198 EFLOPS (exaflops), Lingsheng became the world's first supercomputer to exceed 2 EFLOPS — a milestone that underscores China's growing technological self-reliance despite ongoing semiconductor export restrictions.

## A Long-Awaited Return to the Top

China's last #1 supercomputer was the Sunway TaihuLight, which held the top spot from June 2016 to November 2017. In the years that followed, US systems — Summit, Frontier, and El Capitan — dominated the rankings, while China's presence on the TOP500 list steadily declined due to US export controls on advanced semiconductor technology. According to [Pandaily](https://pandaily.com/china-lingsheng-lineshine-supercomputer-top500-jun2026), TOP500 benchmark co-author Jack Dongarra noted that China had stopped submitting benchmark data in recent years due to these restrictions. Lingsheng's return to #1 represents a significant reversal of that trend.

## What Makes Lingsheng Different

Lingsheng's most distinctive feature is its **pure CPU architecture** — a stark contrast to virtually every other top-tier supercomputer, which relies on CPU+GPU heterogeneous designs. The system uses 304-core 1.55GHz LX2 processors built on the ARMv9 architecture, with lineage tracing back to Huawei's Kunpeng chip family. Across 92 cabinets, the system packs 13.79 million cores running the domestic Kylin operating system, as detailed by [IT之家](https://www.ithome.com/0/967/581.htm).

"What distinguishes LineShine from virtually every other top-tier supercomputer is its pure CPU architecture," Pandaily reported. "While most leading systems rely on CPU+GPU heterogeneous designs... LineShine uses standard microprocessors exclusively, with no GPU or specialized AI accelerators."

## Performance and Benchmarks

Lingsheng achieved #1 on both the standard HPL (LINPACK) benchmark at 2.198 EFLOPS and the HPCG (High-Performance Conjugate Gradient) benchmark, which measures real-world computational throughput. In the HPL-MxP mixed-precision benchmark tailored for AI workloads, it placed fourth worldwide at 7.92 exaflops. The system consumes approximately 42.2 MW of power, yielding an energy efficiency of 52.07 Gigaflops/W — ranking 50th on the GREEN500 list.

By comparison, the #2 system — the US Department of Energy's El Capitan at Lawrence Livermore National Laboratory — achieves 1.809 EFLOPS while consuming 29.7 MW, making it more energy-efficient. Lingsheng uses roughly 40% more power for a 20% performance gain, a trade-off that reflects its all-CPU design approach.

## Full-Stack Domestic Localization

According to a commentary published by [People's Daily via Sina Finance](https://finance.sina.com.cn/roll/2026-07-13/doc-inihrsvf2230594.shtml), Lingsheng achieved "full-stack domestic localization" of key components. This includes the LX2 processors (ARMv9 architecture, fabricated likely at SMIC 7nm), the Kylin operating system, the "LingQi" domestic interconnect technology, and domestic HBM memory. "This top-ranking supercomputer system achieved full-stack domestic localization of key components," People's Daily stated, "marking that China's supercomputing industry is accelerating toward independent R&D, independent iteration, and independent leadership."

## Supercomputing vs. AI Computing: An Important Distinction

Independent tech analyst Luke Fan (老范讲故事) offered a nuanced assessment of the achievement. Writing on [his blog](https://lukefan.com/2026/06/29/china-top500-supercomputer-linpack-benchmark-analysis/), Fan emphasized that Lingsheng's #1 ranking is specifically for **FP64 double-precision scientific computing** — a fundamentally different benchmark from AI computing, which prioritizes throughput and speed over precision using lower-precision formats like FP16, FP8, or even FP4.

"The gold content of Lingsheng's #1 ranking is quite high — fully domestic, pure CPU, ARM architecture, double-precision first," Fan wrote. "But regarding the nanometer process node, they didn't say, so we shouldn't exaggerate on that."

Fan compared the distinction to the difference between a Formula 1 race car and a freight truck: "Supercomputing is like an F1 car — single-point excellence, pursuing极致 precision. An AI center is like a freight convoy of tens of thousands of GPUs, seeking throughput."

## Applications and Broader Significance

Since its deployment, Lingsheng has supported applications in atmospheric and ocean modeling, engineering simulation, materials science, drug discovery, brain science research, scientific AI, aerospace simulation, and weather forecasting. [China News Service](https://www.chinanews.com.cn/gn/2026/06-24/10646023.shtml) reported from ISC 2026 that Lingsheng's chief designer, Lu Yutong, described the system as pioneering "an Online Acceleration all-CPU architecture, breaking traditional CPU-GPU heterogeneous architecture barriers."

Lingsheng's achievement carries implications beyond raw performance. It demonstrates China's ability to build world-class high-performance computing systems despite semiconductor export restrictions, highlights the growing maturity of China's domestic computing ecosystem, and provides critical infrastructure for Chinese scientific research. However, experts caution that this achievement should not be conflated with AI computing leadership, where the US retains advantages through GPU-accelerated systems.

## What's Next

With Lingsheng's debut at #1, the global supercomputing landscape has shifted. The top five now includes Lingsheng (China), El Capitan (US), Frontier (US), Aurora (US), and Jupiter (Germany). As the EU announces a €20 billion plan to build AI "super-factories," and with US export controls still in place, the competition for computing supremacy is entering a new, multi-dimensional phase. The question now is not just who builds the fastest machine, but who can best integrate traditional HPC with the rapidly evolving demands of AI.
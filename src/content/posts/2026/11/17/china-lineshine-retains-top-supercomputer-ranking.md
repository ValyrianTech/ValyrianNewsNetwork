---
story_id: story_9de76eaa
title: China's LineShine Retains No. 1 Supercomputer Ranking
date: '2026-11-17T05:24:00Z'
meta_description: China's LineShine supercomputer in Shenzhen held No. 1 on the TOP500
  and HPCG rankings at SC26, cementing China's lead in high-performance computing.
slug: china-lineshine-retains-top-supercomputer-ranking
read_time_minutes: 5
word_count: 989
tags:
- supercomputing
- LineShine
- TOP500
- HPC
- China technology
- China
categories:
- Technology
- China
style: formal_news
draft: false
---
# China's LineShine Retains No. 1 Supercomputer Ranking

China's homegrown "Lingsheng" supercomputer, known internationally as LineShine, has retained first place on both the global TOP500 ranking and the HPCG benchmark, cementing the country's position at the very top of high-performance computing. The result was announced at the SC26 international supercomputing conference in Chicago, where the 68th edition of the TOP500 list was released.

According to [The Paper](https://www.thepaper.cn/newsDetail_forward_34491261), citing CCTV News, the E-class system installed at the National Supercomputing Center in Shenzhen posted 2.198 exaflops on the Linpack double-precision benchmark — about 21% ahead of the second-place U.S. system, El Capitan, which reached 1.809 exaflops. LineShine also held the top spot on the HPCG ranking at 22 petaflops.

## A Stable Leaderboard

The November ranking is a retention of June's victory rather than a new performance record. The entire top 10 was unchanged from the previous edition. Behind LineShine and El Capitan, Frontier (1.353 exaflops), Aurora (1.012 exaflops), and Germany's JUPITER Booster (1.000 exaflops) completed the group of five systems — the only ones on the list to reach an exaflop on HPL.

In its [official press release](https://new.top500.org/news/top500-leadership-holds-steady-new-system-turnover-falls-historic-low/), the TOP500 project called the result a sign of a maturing deployment cycle. "The ten leading systems did not change since the June edition. Just 27 systems are new, the lowest number ever recorded by a wide margin," the organizers wrote, describing "a mature phase in the current deployment cycle: leadership is stable, the number of newcomers is exceptionally low, and the most visible progress is occurring deeper in the list."

That stability at the top obscures continued growth lower down. The entry threshold for the No. 500 spot rose 7.3% to 2.857 petaflops, and combined performance across all 500 systems climbed 4.4% to 19.57 exaflops.

## Breaking From the GPU Mainstream

LineShine's ascent reflects a deliberate architectural gamble. The system uses an all-CPU design built on custom LX2 304-core processors connected by a proprietary LingQi interconnect, with 13,789,440 cores in total, as [Network World](https://www.networkworld.com/article/4249297/chinas-lineshine-remains-worlds-fastest-supercomputer.html) reported. That sets it apart from the dominant global model of pairing CPUs with GPU accelerators, the approach used by El Capitan, Frontier, and Aurora.

Chinese coverage frames the choice as a statement of self-reliance. According to an interview with chief designer Lu Yutong, dean of Sun Yat-sen University's School of Computer Science, reported by [Icviews](https://www.icviews.cn/news/737/2), the willingness to abandon the global GPU route came from full-stack independence.

> "If we did not have control over the entire chain, we could never have walked a path completely different from the global mainstream," Lu said.

The system is described as fully self-controllable from chips to network, storage, and system software — a pointed claim given U.S. export restrictions on high-end processors to Chinese supercomputing centers since 2015. Chinese commentary has framed those restrictions as a catalyst for indigenous chip development.

## What LineShine Does Not Lead

The headline result comes with important caveats. LineShine dominates on dense double-precision and sparse workloads, but it is not the leader across the board. On the HPL-MxP mixed-precision benchmark — the measure most relevant to AI training and inference — El Capitan leads at 16.7 exaflops, ahead of Aurora (11.6) and Frontier (11.4). LineShine trails on that metric.

The system also trails on energy efficiency. In the Green500 ranking, France's KAIROS remains No. 1 at 73.28 gigaflops per watt, followed by France's ROMEO-2025 and Germany's Levante GPU extension, according to Network World. LineShine's strength lies in raw double-precision performance, achieved without accelerators.

## A Nine-Year Gap Closed

LineShine is the first China-based system to lead the TOP500 since Sunway TaihuLight in 2017. It is the fifth exascale-class system to sit atop the list and the second Chinese system — after Tianhe-2 — to claim both the TOP500 and HPCG crowns simultaneously, a "double champion" status it first achieved in June 2026. Tianhe-2 had held a similar dual distinction starting in 2013.

Holding both titles is widely viewed as proof of balanced design. The TOP500's HPL benchmark measures peak floating-point throughput, while HPCG measures sparse linear-algebra performance that better reflects real scientific and engineering simulation, exposing data-movement and communication bottlenecks. A system that leads on both demonstrates that peak power translates into practical efficiency.

The Shenzhen center reports that LineShine has already supported 22 applications at the ten-million-core scale and adapted more than 220 domain applications, spanning climate and ocean science, energy and materials, biomedicine, brain simulation, and large-model training. An XLSDFT scientific application built on the system was shortlisted for the 2026 ACM Gordon Bell Prize, a top honor in the field.

## Where the Growth Is Going

The static top 10 points to a broader shift in how the world's computing power is being deployed. TOP500 organizers, citing Epoch AI, noted that five major U.S. hyperscalers owned an estimated 71% of global AI compute capacity as of the fourth quarter of 2025, with much of that capacity housed in enormous commercial clusters.

"This suggests that growth has indeed shifted toward AI factories, and from capability systems to capacity systems," the organizers wrote. In other words, the most powerful new hardware is increasingly going into private AI datacenters rather than into the national systems that the TOP500 measures.

## What to Watch

LineShine's lead is secure for now, but the next shift at the top depends on when a new generation of large, energy-efficient systems reports measured results — and U.S. exascale successors, along with potential new Chinese systems, could reshape the picture in 2027.

Two open questions remain. First, TOP500 results are largely self-reported by vendors and sites; no independent third-party audit of LineShine's measured performance has been published. Second, how well the all-CPU architecture performs on production AI and mixed-precision workloads relative to GPU-based rivals remains to be seen — a gap that LineShine's HPL-MxP ranking makes plain. Holding first place on two benchmarks is a milestone. Whether the all-CPU path can win the workloads that increasingly define computing power is the harder test still to come.

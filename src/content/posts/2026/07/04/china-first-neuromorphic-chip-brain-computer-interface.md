---
story_id: story_2a3de3fd
title: China Debuts First Neuromorphic Chip for Brain Interfaces
date: '2026-07-04T09:09:00Z'
meta_description: Chinese researchers unveil the first neuromorphic chip based on
  phase-change memristors, achieving 478x speedup over GPUs in brain tasks.
slug: china-first-neuromorphic-chip-brain-computer-interface
read_time_minutes: 4
word_count: 778
tags:
- neuromorphic chip
- brain-computer interface
- China technology
- Peking University
- semiconductors
- China
categories:
- Technology
- Science
style: formal_news
draft: false
---
# China Debuts First Neuromorphic Chip for Brain Interfaces

In a breakthrough published in the journal *Science*, a team of Chinese researchers has developed the world's first neuromorphic system chip based on phase-change memristors, compressing single-step computation latency to just 2.12 milliseconds and achieving up to 478 times the speed of advanced GPUs in brain cortex reconstruction tasks. The chip, developed by Professor Yang Yuchao of Peking University's School of Integrated Circuits in collaboration with researcher Song Zhitang from the Shanghai Institute of Microsystem and Information Technology, Chinese Academy of Sciences, solves a half-century bottleneck in real-time neuromorphic computing.

## The Half-Century Challenge

Neuromorphic systems combine the representational power of neural networks with the continuous evolution mechanisms of differential equations, enabling them to reconstruct smooth, precise 3D brain structures from incomplete, noisy data. Applications range from physical world modeling and computational imaging to brain-computer interfaces (BCI).

However, for 50 years, these systems faced a fundamental barrier: the von Neumann architecture, which separates storage and computation. Solving neuromorphic differential equations requires repeatedly moving massive intermediate variables between memory and processor, creating enormous latency and power consumption that prevented real-time, high-precision operation. As [Xinhua News](https://www.news.cn/tech/20260704/0287498f97b3494ba99a09f209f1cc14/c.html) reported, this "data factory" model wasted enormous time in data transportation.

## The Breakthrough: Controllable Compute-in-Memory

The team's key innovation lies in a paradigm they call "controllable compute-in-memory" (可控存内计算). Rather than fighting against a physical property long considered a defect — the conductance drift of phase-change memory (PCM) — they harnessed it.

According to [Guangming Daily](https://epaper.gmw.cn/gmrb/html/content/202607/04/content_18315.html), within a specific time window, the conductance change of PCM is predictable and precisely controllable. The team used this property to encode the effective integration step size directly into the conductance state of the PCM, allowing the device's own physical evolution to perform step-size searching — eliminating the need for digital circuits to repeatedly calculate, compare, and judge.

Simultaneously, neural network weights were mapped onto the multi-level conductance states of PCM, enabling matrix multiply-accumulate operations directly within the same array. Both core computational tasks were unified and integrated into a single 0.28 mm² compute-in-memory array fabricated on a 40nm process, running at 50 MHz.

## Performance That Redefines Possibilities

The results are striking. As Professor Yang Yuchao told [Jiwei/laoyaoba](https://laoyaoba.com/n/1056632), the chip achieves a single-step iteration latency of 2.12 milliseconds — the first time neuromorphic hardware has entered the millisecond era. In equivalent computation tasks, it delivers:

- **3.82x to 36.27x speedup** over current state-of-the-art dedicated accelerators (ASICs)
- **50.38x to 478.18x speedup** over the NVIDIA A100 GPU in brain cortex reconstruction
- **Power consumption reduced** to just 1/24.73 to 1/11.75 of dedicated accelerators

In high-fidelity brain cortex surface reconstruction tasks, the chip produces smooth, topologically consistent 3D mesh models that accurately capture complex cortical folding structures while effectively suppressing artifacts and self-intersection defects common in traditional methods.

## Applications in Brain-Computer Interfaces and Medicine

This breakthrough opens entirely new possibilities for brain-computer interfaces and neurological disease diagnosis. Professor Yang noted, as reported by [QQ News/MyDrivers](https://news.qq.com/rain/a/20260704A0632O00), that individualized, dynamic brain digital twins become possible with this hardware foundation. Specific applications include:

- **Real-time neural signal parsing** for next-generation BCI systems
- **Intraoperative neural navigation** providing real-time guidance during brain surgery
- **Early screening for Alzheimer’s disease** and personalized interventions
- **Monitoring of Parkinson’s disease** through subtle brain structure and function changes

The technology transitions BCI from simple signal recognition to real-time brain state modeling and intelligent interaction.

## Broader Implications for China’s Tech Landscape

This breakthrough arrives amid intensifying US-China technology competition, particularly in semiconductors and AI. Notably, the chip uses mature 40nm process technology, which is not subject to US export restrictions on advanced nodes. It demonstrates a fundamentally different approach to post-Moore’s Law computing — letting device physics do the computational work rather than relying solely on transistor scaling.

The research was supported by multiple national-level programs, including the New Cornerstone Investigator Project, the National Key R&D Program, and the National Natural Science Foundation of China. China’s government has identified BCI as a strategic emerging industry in its 2026 Government Work Report, and the global BCI market is projected to exceed $10 billion by 2030.

## What’s Next

While the chip is currently a research prototype rather than a commercial product, the path forward is promising. The team’s “controllable compute-in-memory” paradigm provides a new blueprint for energy-efficient, real-time neuromorphic computing. Future work may focus on scaling the technology to more advanced process nodes and developing specific applications in medical diagnostics and brain-computer interfaces.

As Professor Yang emphasized, this breakthrough provides a hardware foundation capable of real-time operation for applications that were previously confined to offline processing — bringing us closer to a future where machines can model and understand the brain as it actually works.
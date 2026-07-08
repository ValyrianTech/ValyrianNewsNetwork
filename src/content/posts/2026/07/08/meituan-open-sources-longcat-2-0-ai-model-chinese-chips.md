---
story_id: story_cd57c19f
title: Meituan Open-Sources 1.6T-Parameter AI on Chinese Chips
date: '2026-07-08T08:19:02Z'
meta_description: Meituan open-sources LongCat-2.0, a 1.6-trillion-parameter AI model
  trained on domestic Chinese chips, marking a milestone in AI self-sufficiency.
slug: meituan-open-sources-longcat-2-0-ai-model-chinese-chips
read_time_minutes: 6
word_count: 1175
tags:
- Meituan
- LongCat-2.0
- AI
- Chinese Chips
- Open Source
- China
categories:
- Science & Technology
- Economy
style: analytical_blog
draft: false
---
# Meituan Open-Sources 1.6 Trillion-Parameter AI Model Built on Chinese Chips

Chinese tech giant Meituan has open-sourced LongCat-2.0, a massive 1.6-trillion-parameter artificial intelligence model trained entirely on a 50,000-card cluster of domestically produced Chinese chips. The move marks the first time a trillion-parameter model has completed both pre-training and inference on domestic hardware, representing a significant milestone in China's push for AI self-sufficiency amid escalating US export restrictions on advanced semiconductors.

## The Model That Topped Global Charts Anonymously

Before Meituan revealed its identity, LongCat-2.0 had been quietly dominating global developer platforms under the codename "Owl Alpha" on OpenRouter, an API routing platform. During its anonymous residency, the model processed approximately 10.1 trillion tokens per month — averaging 559 billion tokens daily — and ranked among the top three most-used models globally by call volume, according to [VentureBeat](https://venturebeat.com/technology/meituan-open-sources-longcat-2-0-the-1-6t-near-frontier-agentic-coding-model-thats-been-leading-openrouter-trained-entirely-on-chinese-chips).

The model secured the top ranking on the Hermes Agent workspace, second place on Claude Code deployments, and third place across international OpenClaw environments — all before developers knew it was built by a Chinese food-delivery company.

## Breaking the Nvidia Dependency

What makes LongCat-2.0 a definitive inflection point is its operational independence. The model was trained from scratch on a cluster of over 50,000 domestic Chinese AI ASIC superpods, with chip suppliers including [Huawei](https://www.caixinglobal.com/2026-07-07/meituan-open-sources-16-trillion-parameter-ai-model-built-on-chinese-chips-102461495.html) (Ascend Atlas A2), Moore Threads, and MetaX — all immediately confirming their hardware supports the system.

This stands in contrast to earlier Chinese flagship models. DeepSeek's V4-pro, for instance, relied on domestic chips only for inference — the less computationally intensive phase where a pre-trained model runs to answer queries. LongCat-2.0 used domestic hardware for both inference and the far more demanding pre-training process, during which an AI model digests massive datasets to learn basic patterns.

As analysts at [NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/meituan-open-sources-longcat-2-0-a-1-6t-model-trained-on-chinese-chips/) noted: "If the full-process-on-Chinese-chips claim holds up under independent scrutiny, it suggests China's path around NVIDIA export controls is maturing from 'good enough for inference' to 'good enough to train trillion-parameter frontier models.'"

## Technical Architecture: Efficiency at Scale

LongCat-2.0 is a sparse Mixture-of-Experts (MoE) system with 1.6 trillion total parameters but only 33 to 56 billion active per token (averaging roughly 48 billion), keeping inference costs far below its headline size. It ships with a native 1-million-token context window, made tractable by a custom linear-complexity attention mechanism called LongCat Sparse Attention (LSA).

LSA employs three distinct optimization vectors: Streaming-aware Indexing (SI) that converts fragmented memory access into predictable sequential blocks for efficient High Bandwidth Memory utilization; Cross-Layer Indexing (CLI) that amortizes calculation costs by leveraging stable attention saliency across adjacent hidden layers; and Hierarchical Indexing (HI) that applies a coarse-to-fine, two-stage scoring layout for rapid candidate filtering. The architecture also integrates an N-gram Embedding module that appends 135 billion parameters to a 5-gram token combination framework, expanding the core embedding space by roughly 100-fold.

According to Meituan's [official announcement](https://tech.meituan.com/2026/06/30/LongCat2.0.html), the company overcame significant challenges to train on domestic hardware, tackling hardware faults, communication anomalies, memory pressure, and numerical fluctuations at the 50,000-card scale. The team achieved a steady-state throughput exceeding 1 trillion tokens per day while reducing the average daily failure rate by over 70%.

The model also incorporates a novel post-training architecture called MOPD (Multi-Teacher Optimization via Mixture of Specialized Experts), which segregates optimization into three independent expert clusters: Agent Experts for tool use and self-correction, Reasoning Experts for multi-hop logic and STEM reasoning, and Interaction Experts for instruction-following and alignment. A dynamic gate-routing mechanism seamlessly fuses these specialized behaviors at runtime, allowing the model to coordinate deep reasoning, stable tool execution, and safe user interaction simultaneously.

## Benchmark Performance: Competitive with Frontier Models

LongCat-2.0 demonstrates strong performance across agentic and coding benchmarks. On SWE-bench Pro, it scored 59.5, edging out OpenAI's GPT-5.5 (58.6) and surpassing Claude Opus 4.6 (57.3). It also achieved 70.8 on Terminal-Bench 2.1, 77.3 on SWE-bench Multilingual, and 73.2 on the general corporate workflow simulator FORTE.

However, the model generally trails premium frontier systems like Claude Opus 4.8 across broad general-agent benchmarks, particularly in complex multi-disciplinary research tasks.

## Geopolitical Context: Filling the Vacuum

The release of LongCat-2.0 arrives at a critical geopolitical moment. The US government has ordered restrictions on access to American frontier AI models, including OpenAI's GPT-5.6 and Anthropic's Claude Fable 5, which was taken entirely offline in response. As VentureBeat reported, these defensive regulatory maneuvers have inadvertently backfired, leaving a wide operational window for global developers seeking affordable, high-performance alternatives.

Chinese open-source models like LongCat-2.0 are filling that gap. The model is released under the permissive MIT license, allowing enterprises to integrate it into proprietary products without restrictions. Its aggressive pricing — $0.30 per million input tokens during the promotional period — undercuts Western competitors by 10 to 100 times.

## Meituan's Transformation: From Delivery App to AI Powerhouse

Founded in March 2010 by Wang Xing, Meituan began as a Groupon-style daily deals website before evolving into one of China's dominant "super apps." Following a massive 2015 merger with Dianping, the Beijing-based company now claims over 770 million annual transacting users and supports a network of more than 14.5 million merchants.

Meituan's pivot toward AI infrastructure began in earnest with its 2023 acquisition of AI startup Light Year for approximately $285 million. Research and development spending jumped 22% year-on-year to 7 billion yuan in the first quarter of 2026. The company released LongCat-Flash, a 560-billion-parameter MoE model, in late 2025, followed by LongCat-Flash-Thinking, before unveiling LongCat-2.0 on June 30, 2026. Meituan's stock closed up 4.7% on the announcement day.

## What This Means for the Global AI Landscape

LongCat-2.0 lands at the intersection of two major trends: the steady march of open-weight Chinese models toward the frontier, and the geopolitics of AI compute. A delivery company shipping a top-three-by-usage agentic coding model is itself notable — but doing it on a fully domestic training stack is the part that will be studied most closely.

For global developers and enterprises, the model offers an immediately testable alternative for agentic coding workloads. The combination of an MIT license, a 1-million-token context window, and zero-cost context cache hits fundamentally changes the economics of large-scale autonomous software development.

However, outstanding questions remain. Has the "full domestic training" claim been independently audited? Which specific Chinese chips were used? The full model weights are still listed as "coming soon" on both GitHub and Hugging Face. Independent verification of these claims will be crucial to understanding whether this represents a genuine breakthrough or a carefully framed milestone.

What is clear is that the landscape of AI development is shifting. As US export controls tighten and Chinese domestic capabilities advance, the era of Nvidia-dominant AI training infrastructure may be giving way to a more fragmented, multipolar compute ecosystem — and Meituan's LongCat-2.0 is the strongest signal yet that China intends to be a leading player in that new order.

For now, developers and enterprises can test LongCat-2.0 immediately through OpenRouter and the LongCat API platform. The model's aggressive pricing, permissive licensing, and strong coding benchmarks make it an attractive option for teams building autonomous software agents — regardless of the geopolitical currents swirling around its creation.
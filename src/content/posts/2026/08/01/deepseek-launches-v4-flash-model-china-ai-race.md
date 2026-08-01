---
story_id: story_19bc1487
title: DeepSeek Launches V4-Flash Model, Escalating China AI Race
date: '2026-08-01T12:46:02Z'
meta_description: DeepSeek releases its V4-Flash model in public beta with enhanced
  agent capabilities and lower API costs, intensifying China's AI race.
slug: deepseek-launches-v4-flash-model-china-ai-race
read_time_minutes: 4
word_count: 713
tags:
- DeepSeek
- V4-Flash
- AI
- China
- Technology
categories:
- Technology
- China
style: formal_news
draft: false
---
# DeepSeek Launches V4-Flash Model, Escalating China AI Race

Chinese artificial intelligence startup DeepSeek has released the official version of its DeepSeek-V4-Flash model, significantly enhancing autonomous agent capabilities and further cutting API costs as competition in China's AI sector intensifies. The update, published in the company's developer documentation on July 31, arrived slightly behind its self-imposed mid-July target and without the highly anticipated V4-Pro iteration, according to [Caixin Global](https://www.caixinglobal.com/2026-08-01/deepseek-releases-official-v4-flash-model-as-chinas-ai-race-intensifies-102470292.html).

## Context

DeepSeek, the Hangzhou-based startup that became a global player with its open-source R1 reasoning model in January 2025, introduced the V4 generation in late April 2026 with 1 million-token context as standard. The V4-Flash preview — a Mixture-of-Experts model with 284 billion total parameters and 13 billion active — became the most-used model on OpenRouter for seven consecutive weeks in early summer. The company announced in late June that the official V4 version was planned for mid-July, a timeline the July 31 launch slightly missed, as [IT之家](https://www.ithome.com/0/970/123.htm) reported.

## Key Developments

In the official [DeepSeek API Change Log](https://api-docs.deepseek.com/updates/), the company said the V4-Flash official release is now in public beta — developers simply set the model name to deepseek-v4-flash to use the latest build. DeepSeek said agent capabilities were "significantly enhanced, with benchmark results far exceeding V4-Pro-Preview," citing scores including 82.7 on Terminal Bench 2.1, 54.4 on DeepSWE, and 70.3 on Toolathlon (verified) across nine agent-focused benchmarks.

Crucially, the company noted that "DeepSeek-V4-Flash-0731 keeps the same model architecture and size as DeepSeek-V4-Flash-Preview, and was only re-post-trained." The performance gains therefore come entirely from post-training rather than scale — a signal that training methods and data quality are carrying increasing weight relative to raw parameter counts.

Pricing reflects the company's cost-focused strategy. The official [Models & Pricing page](https://api-docs.deepseek.com/quick_start/pricing) lists V4-Flash at $0.14 per million input tokens (cache miss), $0.0028 with cache hit, and $0.28 per million output tokens — roughly one-third the cost of V4-Pro. DeepSeek also said it will soon adopt a peak/off-peak pricing policy that doubles prices during peak hours (9:00–12:00 and 14:00–18:00 Beijing time). The official V4-Flash natively supports OpenAI's Responses API format and is specifically adapted for Codex, easing migration of OpenAI-style agent applications to DeepSeek at lower cost. The update leaves V4-Pro unchanged, with DeepSeek saying "the official release of DeepSeek-V4-Pro will follow soon."

## Analysis

The release breaks with the industry's familiar "strong Pro, weak Flash" logic. Commentary published by 凤凰网科技 via [36Kr](https://www.36kr.com/p/3919224296451461) noted that the official Flash now approaches or even exceeds the level of the V4-Pro preview from three months ago on multiple agent benchmarks. While a model with only 13 billion active parameters still trails top-tier closed models such as GPT-5.6 Sol and Claude Opus on the hardest long-horizon tasks, its price-performance makes it a formidable option for high-volume agent and coding workloads.

The timing is significant. On the same day, ByteDance and MiniMax both released new models for one-click AI video creation, and earlier in July Moonshot AI launched its 2.8-trillion-parameter Kimi K3. Commentary across Chinese tech media frames 2026 as the year of the agent — autonomous planning, tool use, and complex task execution — replacing the long-context race of 2024. DeepSeek founder Liang Wenfeng, as quoted by 凤凰网科技 via 36Kr, framed the shift in stark terms: "AI currently lacks not taste and intuition, but the ability to continuously learn." The company has reportedly built an Agent Harness team led by Cui Tianyi, a Zhejiang University computer science graduate and former Jane Street quant who joined DeepSeek in March.

The release also lands amid a financial turning point. DeepSeek completed its first external funding round in mid-2026, reportedly raising nearly 50 billion yuan (about $7.4 billion) at a valuation of roughly 350 billion yuan, with investors including Tencent, NetEase, and CATL. The company has said it plans to double headcount and focus its expansion on AI agents.

## What's Next

With Flash now in public beta, attention turns to the official V4-Pro release — expected to follow soon — and to Responses API support for V4-Pro, which DeepSeek says should arrive in early August. The rollout of peak/off-peak API pricing will also be watched closely by developers who have come to rely on DeepSeek's low-cost models. As China's AI race accelerates, DeepSeek's bet is clear: make the intelligence powering tomorrow's autonomous applications affordable enough for the majority.

---
story_id: story_45598aa2
title: DeepSeek Releases Official V4-Flash Model in AI Race
date: '2026-08-02T10:10:00Z'
meta_description: DeepSeek launches official V4-Flash model with enhanced agent capabilities
  and aggressive pricing, intensifying China's AI competition.
slug: deepseek-releases-official-v4-flash-model-china-ai-race
read_time_minutes: 6
word_count: 1026
tags:
- DeepSeek
- AI
- China
- Large Language Models
- Technology
categories:
- Technology
style: formal_news
draft: false
---
# DeepSeek Releases Official V4-Flash Model in AI Race

Chinese artificial intelligence startup DeepSeek has released the official version of its DeepSeek-V4-Flash model, introducing significantly enhanced autonomous agent capabilities and further reducing API costs, according to [Caixin](https://www.caixinglobal.com/2026-08-01/deepseek-releases-official-v4-flash-model-as-chinas-ai-race-intensifies-102470292.html). The update, published in the company's developer documentation on July 31, arrived slightly behind its mid-July target and without the highly anticipated V4-Pro iteration.

## A Post-Training Upgrade

The official V4-Flash release is now in public beta on the DeepSeek API under the model name `deepseek-v4-flash` (build -0731). According to the [DeepSeek API change log](https://api-docs.deepseek.com/updates/), the model retains the same architecture and size as the April preview — 284 billion total parameters with 13 billion active parameters in a mixture-of-experts configuration — with performance gains driven entirely by extensive post-training.

"DeepSeek-V4-Flash-0731 keeps the same model architecture and size as DeepSeek-V4-Flash-Preview, and was only re-post-trained," the company stated. "This update only upgrades the DeepSeek-V4-Flash API. The DeepSeek-V4-Pro API and the APP/WEB models are unchanged. The official release of DeepSeek-V4-Pro will follow soon."

The model supports a 1 million-token context window with up to 384K output tokens, and features JSON output, tool calls, the Responses API, and Anthropic API compatibility. Input remains text-only, distinguishing it from multimodal rivals.

## Significantly Enhanced Agent Capabilities

The headline improvement is in autonomous agent performance. DeepSeek-reported benchmark results show dramatic gains over the V4-Pro-Preview across agentic tasks: Terminal Bench 2.1 at 82.7, Cybergym at 76.7, Toolathlon verified at 70.3, and DSBench-FullStack at 68.7. The model also natively supports the Responses API format and is specifically adapted for Codex-style coding agents.

Early developer testing suggests the improvements are tangible. AI developer Zhang Ze, interviewed by [NBD (每日经济新闻)](https://www.nbd.com.cn/articles/2026-08-01/4529304.html), reported that with the same task and prompt, V4-Flash official combined with Hermes completed work in about 40 seconds, compared to 1 minute 47 seconds for GPT-5.6 Sol with Codex. "Of course, Codex's output quality is indeed higher," Zhang acknowledged, "but V4-Flash official's delivery also reached a usable level, above the passing line."

Fellow developer Sun Tao offered a more measured assessment: "Among domestic models, it's better than GLM 5.2, but still somewhat behind GPT 5.6."

## Aggressive Pricing Strategy

DeepSeek continues its role as a price disruptor. According to the official [pricing page](https://api-docs.deepseek.com/quick_start/pricing/), V4-Flash costs just $0.14 per million input tokens (cache miss) and $0.28 per million output tokens — roughly a third of V4-Pro's pricing. Zhang Ze highlighted the cost disparity versus Western competitors: "GPT-5.6 Sol charges $5, $0.5, and $30 per million tokens for input, cached input, and output respectively; while V4-Flash official charges 1 yuan, 0.02 yuan, and 2 yuan RMB — a cost difference of dozens to hundreds of times."

In a practical demonstration, Zhang reported that a 510,000-token task involving local file reading and web information retrieval cost just 0.53 yuan (approximately $0.07).

DeepSeek has also announced a peak/off-peak dynamic pricing mechanism that would double costs during peak hours (9:00-12:00 and 14:00-18:00 Beijing Time), though the effective date has not yet been announced.

## Context: A Year of Rapid Ascension

The V4-Flash official release comes amid a period of extraordinary growth for DeepSeek. The company launched its V4 generation on April 24, 2026, introducing the V4-Pro (1.6 trillion total / 49 billion active parameters) as the world's largest open-weight AI model, alongside the more efficient V4-Flash. Both models support a 1M-token context window and introduced structural innovations including token-wise compression and DeepSeek Sparse Attention, reducing compute costs by up to 90% for Flash and 70% for Pro compared to V3.2, as documented in the [V4 preview release notes](https://api-docs.deepseek.com/news/news260424/).

In May, DeepSeek permanently cut the API price of V4-Pro by 75%, making a temporary promotional discount the standard pricing tier — a move [Caixin reported](https://www.caixinglobal.com/2026-05-25/deepseek-cuts-flagship-ai-model-prices-by-75-as-funding-round-looms-102447441.html) as escalating competition with both domestic and overseas rivals.

The company completed its first external funding round in July, raising approximately 50 billion yuan ($7.4 billion) at a post-money valuation exceeding 350 billion yuan ($52 billion), with investors including Tencent (10 billion yuan), CATL (5 billion yuan), NetEase, and JD.com, as [Caixin detailed](https://www.caixinglobal.com/2026-07-17/deepseek-reaches-52-billion-valuation-in-round-backed-by-tencent-catl-102465358.html). Following the round, DeepSeek launched a sweeping recruitment drive to at least double the size of every department, as [Caixin also reported](https://www.caixinglobal.com/2026-06-27/deepseek-plans-major-hiring-spree-after-74-billion-funding-round-102458157.html).

## China's Intensifying AI Competitive Landscape

The V4-Flash release lands in an increasingly crowded Chinese AI field. Just days earlier, on July 27, Moonshot AI released full weights for Kimi K3 (2.8 trillion parameters), the world's largest open-weights model. Zhipu AI's GLM-5.2 and Tencent's HY3 are also major competitors.

OpenRouter data from July 28 showed Chinese AI models leading global weekly call volume, with the top five slots all occupied by Chinese models: Xiaomi MiMo-V2.5, DeepSeek V4-Flash, Tencent HY3, Zhipu GLM-5.2, and DeepSeek V4-Pro. Chinese models' global market share surpassed US models in early June 2026, reaching approximately 63.5% versus 35.5% by late July.

The V4-Flash preview had already ranked as the most-used model on OpenRouter for seven consecutive weeks during the early summer.

## The Shift Toward Agentic AI

DeepSeek's focus on agent capabilities reflects a broader industry shift from simple chat interfaces toward autonomous agents that can execute real-world tasks. The company has been investing heavily in "Harness" technology — the infrastructure layer that enables AI agents to perform complex, multi-step operations. The V4-Flash release notes reference the DeepSeek Harness minimal mode as the framework used for benchmark testing, with the full Harness announced as "coming soon."

As AI competition moves from model capabilities to task delivery, DeepSeek's combination of aggressive pricing and enhanced agent performance positions it strongly in the emerging agent economy. The company's [OrcaRouter analysis](https://www.orcarouter.ai/blog/deepseek-v4-flash-official-release) notes that V4-Flash's low active-parameter count keeps inference fast and cheap while the large expert pool preserves quality — a design philosophy that has made it one of the best value-per-token options in 2026.

## What to Watch Next

With V4-Flash now officially released, attention turns to the upcoming official release of DeepSeek-V4-Pro, which the company says will follow soon. The implementation of peak/off-peak pricing and the debut of DeepSeek Harness will also be key developments to monitor. As China's AI race intensifies, DeepSeek's ability to maintain its cost advantage while pushing agent capabilities forward will determine whether it can sustain its position at the forefront of the global open-source AI movement.

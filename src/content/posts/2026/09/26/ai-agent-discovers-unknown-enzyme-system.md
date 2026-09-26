---
story_id: story_0c23b909
title: AI Agent Finds Unknown Enzyme System
date: '2026-09-26T05:00:00Z'
meta_description: Anthropic says its Claude agents autonomously discovered a CRISPR-like
  enzyme system in phage DNA, but its function remains unproven.
slug: ai-agent-discovers-unknown-enzyme-system
read_time_minutes: 6
word_count: 1060
tags:
- AI
- biotechnology
- gene-editing
- Anthropic
- CRISPR
- China
categories:
- Science
- Technology
style: formal_news
draft: false
---
# AI Agent Finds Unknown Enzyme System

An AI agent has autonomously discovered a previously unknown enzyme system hidden in viral DNA, in a finding that highlights the growing role of AI-driven research in the biological sciences. The discovery was reported by Chinese media, including [People's Daily](http://finance.people.com.cn/n1/2026/0926/c1004-40805763.html), which cited a report from Science and Technology Daily.

The system was identified on September 23 by Anthropic, the US AI company, using its Claude models. A cluster of roughly 950 Claude agents worked in parallel for about 21.5 hours with no human intervention during the computational search, according to [Anthropic's announcement](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system).

## What Was Found

The system, which Anthropic has named ART (array-associated reverse transcriptases), consists of three parts: a reverse transcriptase that copies RNA into DNA; an adjacent partner gene of unknown function; and a long array of evenly spaced DNA repeat sequences that resembles the architecture of CRISPR.

According to Anthropic, the discovery unfolded after one of the agents flagged what its own reasoning log described as a "spectacular" tandem repeat array sitting next to a gene for an unusual reverse transcriptase. "After 21 hours spent searching this data by roughly 950 agents using 210 million tokens, one of the agents spotted something remarkable: a repeating pattern of DNA sequences that occurs next to the gene for an odd-looking RT," the company wrote.

The system was found mainly in bacteriophages — viruses that infect bacteria — particularly in "jumbo phages." The underlying reverse transcriptase had been identified in earlier studies, but the repeat array and the accessory protein had gone unnoticed.

## A Discovery That Echoes CRISPR

The combination of features — a reverse transcriptase, a non-coding repeat array, and an accessory protein — has only ever been found together in a handful of systems, all of which are programmable and perform operations such as cutting, copying, and pasting DNA. CRISPR, the gene-editing technology, is the most famous of these. So are retrons.

Anthropic was careful to note the limits of the finding. "Although we don't yet know its function, the system that Claude discovered has a set of characteristics that have only ever been found together in a handful of other systems, all of which are programmable and perform operations like cutting, copying, and pasting DNA," the company stated.

The observation has precedent. Restriction enzymes, first found in bacterial immune systems, became the basis for recombinant DNA technology. Taq polymerase, recovered from a Yellowstone hot spring bacterium, made PCR possible. CRISPR itself began as an unusual bacterial repeat sequence — which is why a strange repeat array paired with an unusual protein is treated as a valuable lead, though it is no guarantee of a similar future.

## A Genuine Breakthrough, With Caveats

Anthropic explicitly states that scientists still do not know the system's primary function and have not demonstrated that it can edit DNA like a mature gene-editing tool. The evidence stops at sequence analysis and transcriptome data.

The announcement drew a mixed response from researchers. Feng Zhang, the CRISPR pioneer and professor at MIT and the Broad Institute who reviewed the pre-print, endorsed it as "an exciting example of how AI agents can contribute to biological discovery," adding that the identification of RNA-repeat arrays associated with reverse transcriptases is "genuinely intriguing and merits further investigation."

Others were more skeptical. Lucas Harrington, who earned his PhD in the lab of CRISPR pioneer Jennifer Doudna, said finding a strange gene cluster and repeat sequence is often the easy part. "The hard part — and where the real discovery lies — is figuring out what this system actually does, and Anthropic's research has not done that yet," he said.

A reproducibility problem compounds the doubt. According to [Zhidx](https://tech.ifeng.com/c/8wfxoSixH8y), which published a detailed technical breakdown, the team re-ran the same task ten times under the same framework. Nearly all completed runs touched the ART locus and two pursued the lineage further, but none of the agents read the upstream DNA — so every repeat run missed the array. The company attributes this to the vast search space of reverse transcriptases and the non-deterministic behavior of the agents, meaning the original discovery was partly coincidental.

Anthropic's paper is also a self-report on its own models, based on a pre-print that has not been peer-reviewed.

## Why It Matters

The broader significance lies less in the enzyme itself than in what the search demonstrated. AI handled the data retrieval, candidate screening, and hypothesis generation, while the wet-lab work — traditional biological experiments — was performed by human scientists. Anthropic says that if genome mining can be scaled, expert analyses that normally take weeks or months could be compressed to hours.

That prospect has commercial weight. As [Cailianshe](https://www.163.com/dy/article/L7IT4OAG05198CJN.html) reported, gene-editing stocks fell on the day of the announcement: CRISPR Therapeutics dropped 5.54%, Beam Therapeutics fell 6.02%, and Prime Medicine slid 11.58%. The company has moved aggressively into the field, acquiring the AI drug-discovery startup Coefficient Bio for $400 million in April 2026 and partnering with Novo Nordisk and Bristol Myers Squibb.

In the version of the story carried by [Zhiyaoju](https://news.pedaily.cn/202609/569623.shtml), the emphasis fell on the milestone itself: a first-of-its-kind autonomous scientific discovery produced in 21 hours of zero human intervention.

The technical details, described in [Anthropic's preprint](https://www-cdn.anthropic.com/22573675ada52a8ca8a97a1a4b4326b2f208a071.pdf), suggest a system distinct from CRISPR. ART spacers run 120–220 bases long, compared with CRISPR's roughly 30; no cas genes appear near ART loci; and the ART reverse transcriptase carries about 180 extra amino acids at its head. Researchers identified 95 distinct reverse transcriptase clusters, 28 of which carry detectable repeat arrays. In one validation using published phage infection data, array-derived RNA reached up to 8 percent of total phage RNA fifteen minutes after infection.

## What to Watch

Whether ART becomes anything more than an intriguing sequence is now a question for the laboratory. The critical unanswered questions — whether the reverse transcriptase is active, whether the repeat RNA is its substrate, and what role the system plays in the phage — remain open.

Anthropic frames the result as a template as much as a discovery. As the People's Daily commentary put it, discoveries that transformed biology and medicine often began with scientists noticing oddities in nature. Faced with massive biological data, that noticing — long slow, laborious, and expensive — may now be partly automated. The system's function, and its fate, will be settled the old way: in the wet lab.

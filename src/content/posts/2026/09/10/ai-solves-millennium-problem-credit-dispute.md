---
story_id: story_f782d895
title: AI Solves Millennium Problem, Sparking Credit Dispute
date: '2026-09-10T04:20:00Z'
meta_description: OpenAI says an internal AI model solved the Navier-Stokes Millennium
  Prize Problem in 88 hours, igniting a dispute over credit with mathematicians.
slug: ai-solves-millennium-problem-credit-dispute
read_time_minutes: 5
word_count: 918
tags:
- Artificial Intelligence
- Mathematics
- OpenAI
- Research Ethics
- Navier-Stokes
- China
categories:
- Technology
- Science
style: formal_news
draft: false
---
# AI Solves Millennium Problem, Sparking Credit Dispute

OpenAI announced on September 8 that an unreleased internal model organized roughly 10,000 AI agents to produce a proof of the Navier–Stokes existence and smoothness problem — one of the seven Millennium Prize Problems — in just 88 hours, publishing a 166-page paper alongside machine-checked Lean verification code. The claim, which OpenAI framed as a signal that artificial general intelligence has entered frontier scientific discovery, was almost immediately overshadowed by a bitter dispute over research priority and credit.

The controversy centers on Tristan Buckmaster, a mathematician at New York University's Courant Institute, who had been working on closely related fluid-dynamics results with Anthropic researcher Levent Alpöge. Buckmaster alleges that OpenAI may have drawn on his unpublished research and that the company proposed authorship arrangements that excluded Alpöge. OpenAI denies that its researchers or agents saw the pair's work, though it concedes it "cannot completely rule out" that related product data played some role in training.

## The Problem and the Claim

The Navier–Stokes equations describe how fluids move, underpinning everything from aircraft design to weather prediction and blood-flow research. The open question, as [Xinhua](https://www.news.cn/tech/20260910/490068b55c8d445980d779a37d55cf8e/c.html) explained, is whether a three-dimensional fluid that starts smooth can develop a singularity — a point where velocity grows without bound in finite time — or whether smooth solutions persist forever. The Clay Mathematics Institute listed the problem among its Millennium Prize Problems in 2000, attaching a $1 million award.

OpenAI's result does not prove that an unforced flow necessarily stays smooth. Instead, it targets directions C and D of the Clay problem statement, constructing a finite, everywhere-smooth external force under which the smooth solution cannot be maintained for all time. The system reportedly obtained the solution on September 5, after which the company's recently released GPT-6 Astra model spent 17 hours completing the Lean formalization.

The scale was extraordinary. According to [The New York Times](https://cn.nytimes.com/technology/20260909/openai-proof-millennium-problem/), OpenAI deployed up to 10,000 cooperating AI agents, generating roughly 4.9 million agent messages and about 300 billion output tokens, at a cost the company described as several million dollars. "This is a spectacular capstone to the trajectory we have seen over the past 12 months," OpenAI researcher Sébastien Bubeck told the Times.

## A Dispute Over Credit

The achievement quickly became entangled in questions about how it was reached. Buckmaster and Alpöge had been pursuing the same broad strategy — constructing finite-time blow-up under smooth forcing — building on earlier work by mathematicians Diego Córdoba and Luis Martínez-Zoroa. On August 15, the pair achieved a breakthrough on the Boussinesq and Euler equations, and their Euler result passed Lean verification on August 22.

Because the two researchers had used OpenAI's Codex environment to store drafts and derivations, Buckmaster asked whether the internal model had accessed their session data. OpenAI has publicly denied that its researchers or agents reviewed the pair's work before publication. In its statement, however, the company left a carefully worded caveat: while unlikely, it could not entirely exclude that de-identified data generated through its products may have helped improve the model.

A separate flashpoint concerned authorship. According to [QbitAI](https://www.163.com/dy/article/L6D3O03B0511DSSR.html), Buckmaster said Bubeck twice suggested excluding Alpöge from a proposed paper — a claim Bubeck disputes. Bubeck said he never asked to remove Alpöge from the existing Euler paper, and that the discussion concerned a separate proposed paper in which Buckmaster would serve as lead author rewriting OpenAI's Navier–Stokes proof. In that context, Bubeck said, he remarked that "if Levent weren't an Anthropic employee, things would be simpler." Buckmaster also recalled being asked why he was "destroying his own career" — a remark Bubeck confirmed was made but denied carried threatening intent, adding that he apologized.

## A Question of Scope

Even setting the dispute aside, the result's significance depends on interpretation. The core version of the Navier–Stokes problem that mathematicians have pursued for decades concerns whether an unforced flow can spontaneously form a singularity. OpenAI's proof addresses the Clay statement's smoother, externally forced variant — a legitimate reading of the official problem, but not the unforced case that many researchers regard as the ultimate target.

[Scientific American](https://www.scientificamerican.com/article/ai-may-have-just-solved-a-million-dollar-math-problem-the-field-will-never-be-the-same/) called the development a potential turning point, quoting Buckmaster's own description of it as a "Deep Blue–Kasparov moment" for mathematics. The result still awaits independent verification by the mathematics community, and OpenAI has said it will not claim the $1 million Clay prize.

## What the Field Is Watching

The episode has crystallized a deeper anxiety about AI's growing role in frontier mathematics. Fields Medalist Terence Tao, writing on his [blog](https://terrytao.wordpress.com/tag/tristan-buckmaster/), described the Alpöge–Buckmaster work as a remarkable achievement while cautioning that machine-generated proofs may erode human understanding. "Solving problems is very educational," he told the Times. "It's like going to the gym and setting a goal of lifting weights a hundred times. Now AI can solve problems without really gaining any value from it. It's like having a machine lift the weights for you."

Tao also warned that good questions may become scarcer than good answers. "Once someone shows a particular path to the waterfall, people will just take that path," he said. "They won't spend as much time looking for other paths."

For now, the mathematics community faces two unresolved tasks: independently verifying OpenAI's proof, and deciding what credit — and what authorship — AI-assisted discoveries should confer. Buckmaster's four-page public statement, released alongside three fluid-dynamics papers, frames the moment as one demanding "serious and unhurried discussion." Whether the field can supply that discussion while the technology races ahead remains the open question.
